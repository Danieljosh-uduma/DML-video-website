from django.urls import path
from . import views

app_name = 'video'

urlpatterns = [
    path('', views.video_homepage, name='homepage'),
]