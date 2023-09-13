from django.db import models
from interactions.models import Comment, Like, BookMark, SubScribe
from django.contrib.contenttypes.fields import GenericRelation
# Create your models here.



class RssFeedSource(models.Model):
    rss_link = models.CharField(max_length=200)
    parser_name = models.CharField(max_length=100)



class RssPodcastChannelMetaData(models.Model):
    rss_feed = models.ForeignKey(RssFeedSource, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)
    
    description = models.TextField()
    summary = models.TextField(null=True, blank=True)
    encoded_content = models.TextField(null=True, blank=True)
    subtitle = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    
    generator = models.CharField(max_length=50, null=True, blank=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    category = models.CharField(max_length=50, null=True, blank=True)
    link = models.CharField(max_length=300, null=True, blank=True)
    author_name = models.CharField(max_length=100, null=True, blank=True)
    author_email = models.CharField(max_length=100, null=True, blank=True)    # EmailField
    explicit = models.CharField(max_length=50, null=True, blank=True)         # BooleanField
    image_url = models.CharField(max_length=300, null=True, blank=True)       # UrlField
    image_link = models.CharField(max_length=200, null=True, blank=True)      
    image_title = models.CharField(max_length=150, null=True, blank=True)      
    podcast_type = models.CharField(max_length=100, null=True, blank=True)
    copy_right = models.CharField(max_length=100, null=True, blank=True)
    pub_date = models.CharField(max_length=100, null=True, blank=True)        # BooleanField

    # subscribe = GenericRelation(SubScribe)


class PodcastEpisodeData(models.Model):
    channel = models.ForeignKey(RssPodcastChannelMetaData, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    description = models.TextField()
    summary = models.TextField()
    encoded_content = models.TextField()
    subtitle = models.TextField()
    keywords = models.TextField()

    episode_type = models.CharField(max_length=50)
    episode_number = models.IntegerField()

    guid = models.CharField(max_length=150)
    pub_date = models.CharField(max_length=100)        # BooleanField
    explicit = models.CharField(max_length=50)         # BooleanField
    image = models.CharField(max_length=300)
    duration = models.CharField(max_length=100)        # Time
    enclosure_url = models.CharField(max_length=200)   # UrlField
    enclosure_type = models.CharField(max_length=100)
    enclosure_length = models.IntegerField()

    comment = GenericRelation(Comment)
    like = GenericRelation(Like)
    book_mark = GenericRelation(BookMark)