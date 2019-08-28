from django.contrib import admin

# Register your models here.
from .models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'title']

admin.site.register(Post, PostAdmin)

admin.site.register(Comment)