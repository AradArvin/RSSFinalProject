from rest_framework import serializers
from .models import RssFeedSource, RssPodcastChannelMetaData, PodcastEpisodeData


class RssFeedSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RssFeedSource
        fields = [
            'rss_link', 
            'parser_name',
            ]




class RssPodcastChannelMetaDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = RssPodcastChannelMetaData
        fields = [
            'rss_feed', 
            'title', 
            'description', 
            'summary', 
            'encoded_content', 
            'subtitle', 
            'keywords',
            'generator',
            'language',
            'category',
            'link',
            'owner',
            'explicit',
            'image_url',
            'podcast_type',
            'copy_right',
            'pub_date',
            ]
        depth = 2




class PodcastEpisodeDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = PodcastEpisodeData
        fields = [
            'channel',
            'title',
            'description',
            'summary',
            'encoded_content',
            'subtitle',
            'keywords',
            'episode_type',
            'episode_number',
            'link',
            'guid',
            'pub_date',
            'explicit',
            'image',
            'duration',
            'enclosure',
            ]
        depth = 2