from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Video

# Create your views here.
@login_required(login_url='chatroom:login')
def video_homepage(request):
    page = 'videos'
    videos = Video.objects.all()
    context = {'page': page, 'videos':videos}
    return render(request, 'video/homepage.html', context)