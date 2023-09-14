from django.db import models
# from interactions.models import Comment, Like, BookMark, SubScribe
# from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.



class RssFeedSource(models.Model):
    rss_link = models.CharField(max_length=512)
    parser_name = models.CharField(max_length=512)

    def __str__(self) -> str:
        return self.rss_link



class RssPodcastChannelMetaData(models.Model):
    rss_feed = models.ForeignKey(RssFeedSource, on_delete=models.CASCADE)

    title = models.CharField(max_length=512, null=True, blank=True)
    
    description = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    encoded_content = models.TextField(null=True, blank=True)
    subtitle = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)
    
    generator = models.CharField(max_length=512, null=True, blank=True)
    language = models.CharField(max_length=512, null=True, blank=True)
    category = models.CharField(max_length=512, null=True, blank=True)
    link = models.TextField(null=True, blank=True)
    owner = models.CharField(max_length=512, null=True, blank=True)
    explicit = models.CharField(max_length=512, null=True, blank=True)       
    image_url = models.CharField(max_length=512, null=True, blank=True)      
    podcast_type = models.CharField(max_length=512, null=True, blank=True)
    copy_right = models.CharField(max_length=512, null=True, blank=True)
    pub_date = models.CharField(max_length=512, null=True, blank=True)      

    # subscribe = GenericRelation(SubScribe)

    @classmethod
    def fields(cls):
        return [ f.name for f in cls._meta.fields + cls._meta.many_to_many ]
    
    def __str__(self) -> str:
        return self.title


class PodcastEpisodeData(models.Model):
    channel = models.ForeignKey(RssPodcastChannelMetaData, on_delete=models.CASCADE)

    title = models.CharField(max_length=512, null=True, blank=True)

    description = models.TextField(null=True, blank=True)
    summary = models.TextField(null=True, blank=True)
    encoded_content = models.TextField(null=True, blank=True)
    subtitle = models.TextField(null=True, blank=True)
    keywords = models.TextField(null=True, blank=True)

    episode_type = models.CharField(max_length=512, null=True, blank=True)
    episode_number = models.CharField(max_length=512, null=True, blank=True)

    link = models.TextField(null=True, blank=True)
    guid = models.CharField(max_length=512, null=True, blank=True)
    pub_date = models.CharField(max_length=512, null=True, blank=True)     
    explicit = models.CharField(max_length=512, null=True, blank=True)    
    image = models.TextField(null=True, blank=True)
    duration = models.CharField(max_length=512, null=True, blank=True)     
    enclosure = models.CharField(max_length=512, null=True, blank=True)  

    # comment = GenericRelation(Comment)
    # like = GenericRelation(Like)
    # book_mark = GenericRelation(BookMark)

    
    @classmethod
    def fields(cls):
        return [ f.name for f in cls._meta.fields + cls._meta.many_to_many ]

    def __str__(self) -> str:
        return self.title