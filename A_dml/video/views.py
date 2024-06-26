from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='chatroom:login')
def video_homepage(request):
    page = 'videos'
    context = {'page': page}
    return render(request, 'video/homepage.html', context)