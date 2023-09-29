from django.urls import path, include
from .views import *



urlpatterns = [
    path("api/parse/", RssParserAPIView.as_view(), name="parse"),
    path("api/rss/", ListRssSources.as_view(), name="rss_source_api"),
    path("api/channel/<int:pk>/", ChannelsMetaDataList.as_view(), name="rss_channel_api"),
    path("api/channel/<int:pk>/detail", ChannelsMetaDataDetail.as_view(), name="rss_channel_detail_api"),
    path("api/episode/<int:pk>/", ListRssEpisodes.as_view(), name="rss_episodes_api"),
    path("api/episode/<int:pk>/detail/", RssEpisodesDetail.as_view(), name="rss_episodes_detail_api"),
    path("api/rec", Top10ByAllUsersView.as_view(), name="rec"),
]