import requests
import json
import xmltodict
from .models import RssFeedSource, RssPodcastChannelMetaData, PodcastEpisodeData



fields = RssPodcastChannelMetaData.fields()
print(fields)

fields2 = PodcastEpisodeData.fields()
print(fields)



def file_opener(file_name: str) -> json:
    with open("../rss_files/urls.json") as urls:
        url_file = json.load(urls)

    with open("../rss_files/"+file_name+".json") as j_file:
        json_file = json.load(j_file)
    
    return url_file, json_file

