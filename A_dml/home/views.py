from django.shortcuts import render

# Create your views here.
def homepage(request):
    page = 'home'
    context = {'page': page}
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