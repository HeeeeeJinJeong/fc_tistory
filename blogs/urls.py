from django.urls import path

from .views import posts_list, post_detail, post_write, comment_write, post_like

urlpatterns = [
    path('', posts_list, name='posts_list'),
    path('<int:post_id>/', post_detail, name='post_detail'),
    path('write/', post_write, name='post_write'),
    path('comment/write/', comment_write, name='comment_write'),
    path('post_like/', post_like, name='post_like'),
]