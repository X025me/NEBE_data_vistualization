from django.db import models
from data_v.models import NewvoteHoprgeneral, NewvoteRcgeneral
from api.user.models import User
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType


class Message(models.Model):
    pass

class Request(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    status = models.BooleanField(default=False)
    request_description = models.TextField(blank=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    created_date = models.DateField(auto_now_add=True, null=True)
    
    def __str__(self):
        return str(self.owner.email)