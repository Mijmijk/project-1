from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField()
    likes = models.IntegerField()
    dislikes = models.IntegerField()
    data = models.DateTimeField(auto_now_add=True)
    img = models.ImageField(upload_to='images/')