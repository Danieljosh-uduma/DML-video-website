from django.urls import path
from . import views

app_name = 'chatroom'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('room/<str:pk>/', views.room, name='room')
]