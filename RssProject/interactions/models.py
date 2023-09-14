from django.db import models
from accounts.models import CustomUser
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.



class Comment(models.Model):
    opinion = models.TextField()
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    content_type =   models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')




class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    
    content_type =   models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')




class SubScribe(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    content_type =   models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')




class BookMark(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

    content_type =   models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')