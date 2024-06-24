from django.urls import path
from . import views

app_name = 'user'

urlpatterns = [
    path('', views.resource, name='resource'),
    path('profile/<str:pk>/', views.user_profile, name='profile'),
    path('update-profile/', views.update_user, name='update')
]