from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=100, verbose_name="标题")
    content = models.TextField(verbose_name="内容")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}: {} {}".format(self.id, self.title, self.created_at)


class Reply(models.Model):
    post = models.ForeignKey('Post', related_name='replies', related_query_name='reply')
    author = models.ForeignKey('auth.User')
    content = models.TextField(verbose_name="内容")
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return "{}: {}".format(self.id, self.created_at)
