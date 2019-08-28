from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404

from .models import Post


def posts_list(request):
    posts = Post.objects.order_by('-created_at')
    return render(request, 'blogs/posts_list.html', {'posts':posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blogs/post_detail.html', {'post':post})