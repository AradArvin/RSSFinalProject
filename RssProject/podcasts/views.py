from django.shortcuts import render
from .parsers import save_data_to_db
from django.http import HttpResponse
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
    


