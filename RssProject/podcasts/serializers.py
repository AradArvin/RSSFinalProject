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
            'language',
            'category',
            'link',
            'author_name',
            'author_email',
            'explicit',
            'image_url',
            'image_link',
            'image_title',
            'podcast_type',
            'copy_right',
            'pub_date',
            'subscribe',
            ]
        depth = 2


