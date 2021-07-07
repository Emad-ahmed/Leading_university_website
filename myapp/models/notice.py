from django.db import models


class Notice(models.Model):
    title = models.CharField(max_length=120)
    allnotice = models.TextField(blank=True)
    date = models.DateTimeField(
        auto_now_add=True, blank=True)
    noticeimg = models.ImageField(
        upload_to='images/', default="myimg", blank=True)
