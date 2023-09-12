from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.



class Comment(models.Model):
    opinion = models.CharField(max_length=50)

    content_type =   models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')




class Like(models.Model):

    content_type =   models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField()
    content_object=GenericForeignKey('content_type', 'object_id')



