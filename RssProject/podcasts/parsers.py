import json
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




def podcastEpisodeData_object_field_setter(item_tags: json, channel_obj: RssFeedSource):
        for item in item_tags:
            PodcastEpisodeData.objects.create(
            channel = channel_obj,
            title = item.get("title", None),
            description = item.get("description", None),
            summary = item.get("itunes:summary", None),
            encoded_content = item.get("content:encoded", None),
            subtitle = item.get("itunes:subtitle", None),
            keywords = item.get("itunes:keywords", None),
            episode_type = item.get("itunes:episodeType", None),
            episode_number = item.get("itunes:episode", None),
            link = item.get("link", None),
            guid = item.get("guid", None),
            pub_date = item.get("pubDate", None),
            explicit = item.get("itunes:explicit", None),
            image = item.get("itunes:image", None),
            duration = item.get("itunes:duration", None),
            enclosure = item.get("enclosure", None),
            )




def save_data_to_db(file_name: str, url_name: str):
    url_file, json_file = file_opener(file_name)

    feed = RssFeedSource.objects.create(
        rss_link=url_file["urls"][url_name],
        parser_name="universal_rss_parser, save_data_to_db"
        )

    in_tag = json_file["rss"]["channel"]

    
    channel = rssPodcastChannelMetaData_object_field_setter(in_tag, feed)

    
    items_in_tag = in_tag["item"]

    podcastEpisodeData_object_field_setter(items_in_tag, channel)