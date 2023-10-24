from django.conf import settings
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _

from accounts.publishers import publisher
from .models import RssFeedSource, RssPodcastChannelMetaData, PodcastEpisodeData
from .tasks import task_rss_parsing

class RssParserSerializer(serializers.Serializer):
    notice = serializers.CharField(max_length=128, read_only=True)
    rss_link = serializers.URLField(write_only=True, required=False)
        
    def validate(self, attrs):
        
        link = attrs.get("rss_link", None)
        
        if not link:

            for rss_obj in RssFeedSource.objects.all():
                task_rss_parsing.delay(rss_obj.rss_link)
                log_data = {
                "message": f"{rss_obj.rss_name} is updated",
                "status": "UpdateRss"
                }
                publisher(log_data)
        else:
            task_rss_parsing.delay(link)
            log_data = {
                "message": f"{link} rss is being created",
                "status": "ParseRss"
            }

            publisher(log_data)

        validated_data = {
            'notice': _('the rss feed is being parsed')
        }

        return validated_data
    



class RssFeedSourceSerializer(serializers.ModelSerializer):
    channel_url = serializers.SerializerMethodField()
    episode_url = serializers.SerializerMethodField()
    class Meta:
        model = RssFeedSource
        fields = [
            'rss_name', 
            'rss_link',
            'channel_url',
            'episode_url',
            ]
        
        
    def get_channel_url(self, obj):
        return "{}/api/channel/{}/".format(settings.BASE_URL, obj.id)


    def get_episode_url(self, obj):
        return "{}/api/episode/{}/".format(settings.BASE_URL, obj.id)



class ChannelListMetaDataSerializer(serializers.ModelSerializer): # Needs to change
    detail_url = serializers.SerializerMethodField()
    class Meta:
        model = RssPodcastChannelMetaData
        fields = [
            'rss_feed', 
            'title', 
            'description', 
            'category',
            'owner',
            'explicit',
            'podcast_type',
            'copy_right',
            'pub_date',
            'detail_url',
            ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {k: v for k, v in data.items() if v is not None}
    
    def get_detail_url(self, obj):
        return "{}/api/channel/{}/detail".format(settings.BASE_URL, obj.id)



class ChannelDetailMetaDataSerializer(serializers.ModelSerializer): # Needs to change
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




class PodcastEpisodeListSerializer(serializers.ModelSerializer): # Needs to change
    detail_url = serializers.SerializerMethodField()
    class Meta:
        model = PodcastEpisodeData
        fields = [
            'channel',
            'title',
            'description',
            'episode_type',
            'episode_number',
            'link',
            'guid',
            'pub_date',
            'explicit',
            'duration',
            'detail_url',
            ]
        
    def to_representation(self, instance):
        data = super().to_representation(instance)
        return {k: v for k, v in data.items() if v is not None}

    def get_detail_url(self, obj):
        return "{}/api/episode/{}/detail".format(settings.BASE_URL, obj.id)
    



class PodcastEpisodeDetailSerializer(serializers.ModelSerializer): # Needs to change
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