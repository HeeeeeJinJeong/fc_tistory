from django.db import models

# Create your models here.
from users.models import User
from helpers.models import BaseModel
# from taggit.managers import TaggableManager


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)
    likes = models.ManyToManyField(User, related_name='likes', blank=True)
    # tags = TaggableManager()

    def __str__(self):
        return '%s - %s' % (self.user, self.title)

    def total_likes(self):
        return self.likes.count()


class Comment(BaseModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return '%s - %s' % (self.id, self.user)