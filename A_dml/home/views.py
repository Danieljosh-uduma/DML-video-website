from django.shortcuts import render
from .models import FAQs

# Create your views here.
def homepage(request):
    page = 'home'
    questions = FAQs.objects.all()
    context = {'page': page, 'questions':questions}
    return render(request, 'home/homepage.html', context)

def about(request):
    page = 'about'
    context = {'page': page}
    return render(request, 'home/about.html', context)

def team(request):
    page = 'team'
    context = {'page': page}
    return render(request, 'home/team.html', context)

def member(request):
    page = 'member'
    context = {'page': page}
    return render(request, 'home/member.html', context)

def gallery(request):
    page = 'gallery'
    context = {'page': page}
    return render(request, 'home/gallery.html', context)