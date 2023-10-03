from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import filters


from collections import defaultdict
from django.db.models import Count, F
from .models import *
from .serializers import *

# Create your views here.


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000




class RssParserAPIView(APIView): # Done
    permission_classes = (AllowAny,)
    serializer_class = RssParserSerializer

    def post(self, request):
        
        data = request.data
        serializer = self.serializer_class(data=data)
        serializer.is_valid(raise_exception=True)

        return Response(serializer.data, status=status.HTTP_200_OK)




class ListRssSources(generics.ListAPIView): # Done
    queryset = RssFeedSource.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RssFeedSourceSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['rss_name',]
    ordering_fields = ['rss_name',]




class ChannelsMetaDataList(generics.ListAPIView): # Done
    permission_classes = (AllowAny,)
    serializer_class = ChannelListMetaDataSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title',]
    ordering_fields = ['title','pub_date']

    def get_queryset(self):
        id = self.kwargs["pk"]
        queryset = RssPodcastChannelMetaData.objects.all()
        if id is not None:
            queryset = queryset.filter(rss_feed=id)
        return queryset
    



class ChannelsMetaDataDetail(generics.GenericAPIView): # Done
    serializer_class = ChannelDetailMetaDataSerializer
    queryset = RssPodcastChannelMetaData.objects.all()

    def get(self, request, *args, **kwargs):
        channel = self.get_object()
        serializer = self.get_serializer(channel)

        return Response(serializer.data)
    



class ListRssEpisodes(generics.ListAPIView): # Done
    permission_classes = (AllowAny,)
    serializer_class = PodcastEpisodeListSerializer
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title',]
    ordering_fields = ['title','pub_date','duration',]

    def get_queryset(self):
        id = self.kwargs["pk"]
        queryset = PodcastEpisodeData.objects.all()
        if id is not None:
            queryset = queryset.filter(channel=id)
        return queryset




class RssEpisodesDetail(generics.GenericAPIView): # Done
    serializer_class = PodcastEpisodeDetailSerializer
    permission_classes = (AllowAny,)
    queryset = PodcastEpisodeData.objects.all()
    pagination_class = CustomPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['title',]
    ordering_fields = ['title','pub_date','duration',]

    def get(self, request, *args, **kwargs):

        episode = self.get_object()
        serializer = self.get_serializer(episode)

        return Response(serializer.data)
    



class Top10ByAllUsersView(APIView):
    # serializer_class = ""
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    

    def get(self, request):
        # user = self.request.user.id
        episodes = PodcastEpisodeData.objects.all()
        recomended = episodes.annotate(likes=F("like")).annotate(quantity=Count("like")).values("channel__title", "quantity")


        new_dict = defaultdict(int)
        for r in recomended:
            new_dict[r["channel__title"]] += int(r["quantity"])

        recommended = [
            {"rss": name, "likes": qut}
            for name, qut in new_dict.items()
        ]
        sorted_recommendation = sorted(recommended, key=lambda x: x["likes"], reverse=True)

        queryset = list()
        for r in sorted_recommendation:
            queryset.append(r)
        
        queryset = {"data":queryset}

        return Response(queryset, status=status.HTTP_200_OK)
    
