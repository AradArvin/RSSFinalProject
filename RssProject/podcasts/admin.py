from django.contrib import admin
from .models import RssFeedSource, RssPodcastChannelMetaData, PodcastEpisodeData
# Register your models here.


@admin.register(RssFeedSource)
class RssFeedSourceDisplay(admin.ModelAdmin):
    pass


