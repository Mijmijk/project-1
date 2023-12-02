from django.db import models
from django.utils import timezone 

class Video(models.Model):
    embed_code = models.CharField(default = "", max_length=100)
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
