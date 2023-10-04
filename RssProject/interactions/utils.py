from django.db.models import Count
from podcasts.models import *



def podcast_recommendations(user):

    liked_channels = user.like_set.values_list(
        "episode__channel__title", flat=True
    ).distinct()

    matching_channels = RssPodcastChannelMetaData.objects.filter(title__in=liked_channels).distinct()

    recommendations = []
    for channel in matching_channels:
        episodes = PodcastEpisodeData.objects.filter(channel=channel).order_by("-pub_date")
        recommendations.extend(episodes)

    return recommendations[:10]