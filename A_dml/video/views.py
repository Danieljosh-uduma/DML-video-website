from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from .models import Video
from django.db.models import Q

# Create your views here.
@login_required(login_url='chatroom:login')
def video_homepage(request):
    page = 'videos'
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    # videos = Video.objects.filter(
    #     Q(topic__name__icontains=q)|
    #     Q(name__icontains=q)
    # )
    context = {'page': page}#, 'videos':videos}
    return render(request, 'video/homepage.html', context)