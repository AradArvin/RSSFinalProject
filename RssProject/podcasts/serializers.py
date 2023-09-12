from rest_framework import serializers
from .models import RssFeedSource, RssPodcastChannelMetaData, PodcastEpisodeData


class RssFeedSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = RssFeedSource
        fields = [
            'rss_link', 
            'parser_name',
            ]


