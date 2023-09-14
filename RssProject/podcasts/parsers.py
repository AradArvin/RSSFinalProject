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



def rssPodcastChannelMetaData_object_field_setter(meta_tags: json, feed_obj: RssFeedSource):

    channel = RssPodcastChannelMetaData.objects.create(
        rss_feed = feed_obj,
        title = meta_tags.get("title", None), 
        description = meta_tags.get("description", None),
        summary = meta_tags.get("itunes:summary", None),
        encoded_content = meta_tags.get("content:encoded", None), 
        subtitle = meta_tags.get("itunes:subtitle", None), 
        keywords = meta_tags.get("itunes:keywords", None), 
        generator = meta_tags.get("generator", None),
        language = meta_tags.get("language", None),
        category = meta_tags.get("itunes:category", None),
        link = meta_tags.get("link", None),
        owner = meta_tags.get("itunes:owner", None),
        explicit = meta_tags.get("itunes:explicit", None),
        image_url = meta_tags.get("itunes:image", None),
        podcast_type = meta_tags.get("itunes:type", None),
        copy_right = meta_tags.get("copyright", None),
        pub_date = meta_tags.get("title", None)
        )
    return channel


