from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('Our-team/', views.team, name='team'),
    path('contact-us/', views.member, name='member'),
    path('our-gallery/', views.gallery, name='gallery'),
]
