from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from django.utils.translation import gettext_lazy as _

from .models import *
from .serializers import *
from podcasts.serializers import PodcastEpisodeListSerializer
from .utils import podcast_recommendations


# Create your views here.


class CustomPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response(
            {
                "next": self.get_next_link(),
                "previous": self.get_previous_link(),
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )




class LikeAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LikeSerializer

    def post(self, request, episode_id):
        episode = PodcastEpisodeData.objects.get(id=episode_id)
        like, created = Like.objects.get_or_create(user=request.user, episode=episode)

        if created:
            serializer = self.serializer_class(like)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            msg = {'status': _('This episode is already liked!')}
            return Response(msg, status=status.HTTP_200_OK)
        
    
    def delete(self, request, episode_id):
        episode = PodcastEpisodeData.objects.get(id=episode_id)
        try:
            like = Like.objects.get(user=request.user, episode=episode)
            like.delete()
            msg = {'status': _('Unliked!')}
            return Response(msg, status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            msg = {'status': _('This episode is not liked!')}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        



class CommentAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def post(self, request, episode_id):
        episode = PodcastEpisodeData.objects.get(id=episode_id)
        
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=request.user, episode=episode)
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    



class BookMarkAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = BookMarkSerializer

    def post(self, request, episode_id):
        episode = PodcastEpisodeData.objects.get(id=episode_id)
        bookmarked_episode, created = BookMark.objects.get_or_create(user=request.user, episode=episode)

        if created:
            serializer = BookMarkSerializer(bookmarked_episode)
            msg = {'status': _('Episode bookmarked.')}
            return Response(msg, status=status.HTTP_201_CREATED)
        else:
            msg = {'status': _('This episode is already bookmarked')}
            return Response(msg, status=status.HTTP_200_OK)


    def delete(self, request, episode_id):
        episode = PodcastEpisodeData.objects.get(id=episode_id)
        try:
            bookmarked_episode = BookMark.objects.get(user=request.user, episode=episode)
            bookmarked_episode.delete()

            msg = {'status': _('No longer bookmarked')}
            return Response(msg, status=status.HTTP_204_NO_CONTENT)
        except BookMark.DoesNotExist:
            msg = {'status': _('This episode was not bookmarked')}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        



class LikeListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    serializer_class = PodcastEpisodeListSerializer

    def get(self, requset):
        all_likes = Like.objects.filter(user=requset.user).values_list("episode", flat=True)
        episodes = PodcastEpisodeData.objects.filter(id__in=all_likes)

        serializer = self.serializer_class(episodes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    



class BookmarkListAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    serializer_class = PodcastEpisodeListSerializer

    def get(self, requset):
        all_bookmarks = BookMark.objects.filter(user=requset.user).values_list("episode", flat=True)
        episodes = PodcastEpisodeData.objects.filter(id__in=all_bookmarks)

        serializer = self.serializer_class(episodes, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
    



class ReadItemsView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    serializer_class = PodcastEpisodeListSerializer

    def get_queryset(self):
        user = self.request.user

        all_views = ViewdPodcasts.objects.filter(user=user).values_list("episode", flat=True)

        queryset = PodcastEpisodeData.objects.filter(id__in=all_views)

        return queryset
    



class RecommendationAPIView(APIView):
    permission_classes = (IsAuthenticated,)
    pagination_class = CustomPagination
    serializer_class = PodcastEpisodeListSerializer


    def get(self, request):
        user = request.user

        recommendation_data = podcast_recommendations(user)
        serializer = self.serializer_class(recommendation_data, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)