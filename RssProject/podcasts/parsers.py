import requests
import json
import xmltodict
from .models import RssFeedSource, RssPodcastChannelMetaData, PodcastEpisodeData



fields = RssPodcastChannelMetaData.fields()
print(fields)

fields2 = PodcastEpisodeData.fields()
print(fields)

