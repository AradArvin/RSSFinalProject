from django.db import models
from accounts.models import CustomUser
from podcasts.models import PodcastEpisodeData

# Create your models here.



class Comment(models.Model):
    content = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    episode = models.ForeignKey(PodcastEpisodeData, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_accepted = models.BooleanField(default=True)

    def __str__(self) -> str:
        return f"This comment was left by {self.user.username} for {self.episode.title}"




class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    episode = models.ForeignKey(PodcastEpisodeData, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"{self.user.username} liked {self.episode.title}"





class BookMark(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    episode = models.ForeignKey(PodcastEpisodeData, on_delete=models.CASCADE)


    def __str__(self) -> str:
        return f"Bookmark saved by {self.user.username}"




class ViewdPodcasts(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    episode = models.ForeignKey(PodcastEpisodeData, on_delete=models.CASCADE)
    viewed_at = models.DateTimeField(auto_now_add=True)


    def __str__(self) -> str:
        return f"Viewd by {self.user.username}"










class SubScribe(models.Model):# Unused for now.
    subscribed = models.ForeignKey(CustomUser, on_delete=models.CASCADE)