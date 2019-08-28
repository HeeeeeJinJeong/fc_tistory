from django.db import models

# Create your models here.
from users.models import User
from helpers.models import BaseModel


class Post(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return '%s - %s' % (self.user, self.title)