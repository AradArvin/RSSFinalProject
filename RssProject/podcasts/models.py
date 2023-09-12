from django.db import models
# Create your models here.



class RssFeedSource(models.model):
    rss_link = models.CharField(max_length=200)
    parser_name = models.CharField(max_length=100)



class RssPodcastChannelMetaData(models.Model):
    rss_feed = models.ForeignKey(RssFeedSource, on_delete=models.CASCADE)

    title = models.CharField(max_length=100)

    description = models.TextField()
    summary = models.TextField()
    encoded_content = models.TextField()
    subtitle = models.TextField()
    keywords = models.TextField()

    language = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    link = models.CharField(max_length=300)
    author_name = models.CharField(max_length=100)
    author_email = models.CharField(max_length=100)    # EmailField
    explicit = models.CharField(max_length=50)         # BooleanField
    image_url = models.CharField(max_length=300)       # UrlField
    image_link = models.CharField(max_length=200)      
    image_title = models.CharField(max_length=150)      
    podcast_type = models.CharField(max_length=100)
    copy_right = models.CharField(max_length=100)
    pub_date = models.CharField(max_length=100)        # BooleanField



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

