from turtle import mode
from django.db import models
from django.conf import settings

# Create your models here.

class Relation(models.Model):
    follower = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='followers')
    following = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='following')

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['follower', 'following'], name='unique_following')
        ]

class BlogPost(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    created_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class PostComment(models.Model):
    txt = models.TextField()
    posted_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)

class PostLikes(models.Model):
    liked = models.BooleanField()
    liked_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)
    blog_post = models.ForeignKey(BlogPost, on_delete=models.CASCADE)