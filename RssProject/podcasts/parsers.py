import json
from .models import *
from .utils import universal_rss_parser



def rssPodcastChannelMetaData_object(meta_tags: json, feed_obj: RssFeedSource):
    list_obj = list()
    if not RssPodcastChannelMetaData.objects.filter(rss_feed=feed_obj, title=meta_tags.get("title", None)).exists():
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
  




def podcastEpisodeData_list_objects(item_tags: json, channel_obj: RssPodcastChannelMetaData):
        list_obj = list()
        for item in item_tags:
            if not PodcastEpisodeData.objects.filter(channel=channel_obj, enclosure=item.get("enclosure", None)).exists():
                episode_object = PodcastEpisodeData(
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
                list_obj.append(episode_object)
        
        return list_obj




def create_episode_objects(list_of_obj: list):
     
    PodcastEpisodeData.objects.bulk_create(list_of_obj, ignore_conflicts=True)




def save_data_to_db(rss_link: str):

    xml_json = universal_rss_parser(rss_link)
    xml_channel = xml_json["rss"]["channel"]
    xml_episodes = xml_channel["item"]

    if not RssFeedSource.objects.filter(rss_link=rss_link).exists():
        feed = RssFeedSource.objects.create(
            rss_link=rss_link,
            rss_name=xml_channel["title"]
            )
    else: 
        feed = RssFeedSource.objects.get(rss_link=rss_link)

    in_tag = xml_channel
    channel = rssPodcastChannelMetaData_object(in_tag, feed)
    
    items_in_tag =xml_episodes
    list_episode_objs = podcastEpisodeData_list_objects(items_in_tag, channel)

    create_episode_objects(list_episode_objs)

