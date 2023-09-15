from django.shortcuts import render
from .parsers import save_data_to_db
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from .models import RssFeedSource, RssPodcastChannelMetaData, PodcastEpisodeData
from .serializers import RssFeedSourceSerializer, RssPodcastChannelMetaDataSerializer, PodcastEpisodeDataSerializer

# Create your views here.

def save_to_db(request):

    save_data_to_db("com_apology-line","TheApologyLine")
    save_data_to_db("fm_bibleinayear_rss","TheBibleInAYear")
    save_data_to_db("com_qm_9xx0g","CrimeJunkie")
    save_data_to_db("fm_WWO3519750118","TheDanBonginoShow")
    save_data_to_db("com_54nAGcIl","TheDaily")
    save_data_to_db("fm_EMPBC2962078635","TheLincolnProject")
    
    return HttpResponse('OK')



class ListRssSources(APIView):

    def get(self, request):
        sources = RssFeedSource.objects.all()
        serializer = RssFeedSourceSerializer(sources, many=True)
        return Response(serializer.data)
    


class ListRssChannels(APIView):

    def get(self, request):
        channels = RssPodcastChannelMetaData.objects.all()
        serializer = RssPodcastChannelMetaDataSerializer(channels, many=True)
        return Response(serializer.data)
    


class RssChannelDetail(GenericAPIView):
    serializer_class = RssPodcastChannelMetaDataSerializer

    def get_object(self):
        pk = self.kwargs["pk"]

        queryset = RssPodcastChannelMetaData.objects.filter(pk=pk)

        if not queryset.exists():
            raise Http404("Podcast not found")

        return queryset.first()

    


class ListRssEpisodes(APIView, PageNumberPagination):

    page_size = 10
    def get(self, request):
        episodes = PodcastEpisodeData.objects.all()
        result = self.paginate_queryset(episodes, request, view=self)
        serializer = PodcastEpisodeDataSerializer(result, many=True)
        return self.get_paginated_response(serializer.data)