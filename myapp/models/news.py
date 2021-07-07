from django.db import models


class News(models.Model):
    title = models.CharField(max_length=120)
    allnews = models.TextField(blank=True)
    date = models.DateTimeField(
        auto_now_add=True, blank=True)
    newsimg = models.ImageField(
        upload_to='images/', default="myimg", blank=True)
