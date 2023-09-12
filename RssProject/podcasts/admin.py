from django.contrib import admin
from .models import RssFeedSource, RssPodcastChannelMetaData, PodcastEpisodeData
# Register your models here.


@admin.register(RssFeedSource)
class RssFeedSourceDisplay(admin.ModelAdmin):
    pass



@admin.register(RssPodcastChannelMetaData)
class RssPodcastChannelMetaDataDisplay(admin.ModelAdmin):
    pass


