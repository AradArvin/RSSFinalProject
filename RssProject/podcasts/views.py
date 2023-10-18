from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework import generics
from rest_framework import filters

from .models import *
from .serializers import *
from interactions.models import ViewdPodcasts
# Create your views here.


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )




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

        if request.user.exists():
            user = request.user

        if user.is_authenticated:
            ViewdPodcasts.objects.get_or_create(user=user, episode=episode)

        return Response(serializer.data)
    

