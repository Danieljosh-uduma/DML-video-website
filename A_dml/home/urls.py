from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('not-found/', views.not_found, name='not'),
    path('contact-us/', views.contact, name='contact'),
    path('services/', views.services, name='service')
]

