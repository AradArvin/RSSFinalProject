from django.urls import path
from .views import *

urlpatterns = [
    path("save/", save_to_db, name="save"),
    path("api/feed/", ListRssSources.as_view(), name="rss_source_api"),
    path("api/channel/", ListRssChannels.as_view(), name="rss_channel_api"),
    path("api/episodes/", ListRssEpisodes.as_view(), name="rss_episodes_api"),
]