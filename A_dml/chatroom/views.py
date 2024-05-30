from django.shortcuts import render, redirect
from .models import Topic, Room
from .forms import RoomForm

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

def create_room(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chatroom:homepage')
    context = {'form': form}
    return render(request, 'chatroom/create_room.html', context)

def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('chatroom:homepage')
    context = {'form': form}
    return render(request, 'chatroom/create_room.html', context)

def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('chatroom:homepage')
    context = {'room':room}
    return render(request, 'chatroom/delete_room.html', context)