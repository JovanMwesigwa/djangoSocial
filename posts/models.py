from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import (
    pre_save,
    post_save
)


# Create your models here.
class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    # likes = models.ManyToManyField("LikePost", blank=True)
    likes = models.ManyToManyField(User, blank=True, related_name='post_likes')
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'Post by {}'.format(self.author)


"""
class LikePost(models.Model):
    liked_post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    liker = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    date_liked = models.DateTimeField(auto_now_add=True)
"""