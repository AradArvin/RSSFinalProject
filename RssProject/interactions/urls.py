from django.urls import path
from .views import *


urlpatterns = [
    path('api/like/<int:episode_id>/', LikeAPIView.as_view(), name='like'),
    path('api/comment/<int:episode_id>/', CommentAPIView.as_view(), name='comment'),
    path('api/bookmark/<int:episode_id>/', BookMarkAPIView.as_view(), name='bookmark'),
    path('api/like-list/', LikeListAPIView.as_view(), name='like_list'),
    path('api/bookmark-list/', BookmarkListAPIView.as_view(), name='bookmark_list'),
    path('api/read-items/', ReadItemsView.as_view(), name='read_items'),
    path('api/recommendations/', RecommendationAPIView.as_view(), name='recommendations'),
]