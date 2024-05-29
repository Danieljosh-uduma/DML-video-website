from django.shortcuts import render
from .models import Topic, Room

# Create your views here.
def homepage(request):
    topics = Topic.objects.all()
    rooms = Room.objects.all()
    context = {'topics':topics, 'rooms':rooms}
    return render(request, 'chatroom/homepage.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'chatroom/room.html', context)