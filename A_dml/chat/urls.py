from django.urls import path
from . import views

app_name = 'chatroom'

urlpatterns = [
    path('login/', views.login_page, name='login'),
    path('logout/', views.logout_page, name='logout'),
    path('register/', views.register_page, name='register'),
    
    path('', views.homepage, name='homepage'),
    path('room/<str:pk>/', views.room, name='room'),
    
    path('create-room/', views.create_room, name='create-room'),
    path('suggest-room/', views.suggest_room, name='suggest-room'),
    path('update-room/<str:pk>/', views.update_room, name='update-room'),
    path('delete-room/<str:pk>/', views.delete_room, name='delete-room'),
    path('delete-message/<str:pk>/', views.delete_message, name='delete-message'),
    
    path('topics/', views.topics, name='topic'),
    path('activities/', views.activities, name='activity')
]