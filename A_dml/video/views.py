from django.shortcuts import render

# Create your views here.
def video_homepage(request):
    page = 'videos'
    context = {'page': page}
    return render(request, 'video/homepage.html', context)