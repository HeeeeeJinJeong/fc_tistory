from django.urls import path
from .views import register, UserInformation


urlpatterns = [
    path('register/', register, name='register'),
    path('user/', UserInformation.as_view(), name='user')
]