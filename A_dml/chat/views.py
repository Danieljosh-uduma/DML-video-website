from django.shortcuts import render, redirect
from .models import Topic, Room
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q

# Create your views here.

def login_page(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('user:resource')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exist!!')
            
        user = authenticate(request, username=username, password=password) 
         
        if user is not None:
            login(request, user)
            return redirect('user:resource')
        else:
            messages.error(request, 'incorrect username or password')
        
    context= {'page':page}
    return render(request, 'chatroom/register.html', context)

def logout_page(request):
    logout(request)
    return redirect('home:homepage')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('chatroom:homepage')
    
    form = UserCreationForm
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('user:resource')
        
    context = {'form': form}
    return render(request, 'chatroom/register.html', context)
    
@login_required(login_url='chatroom:login')
def homepage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(description__icontains=q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'topics':topics, 'rooms':rooms}
    return render(request, 'chatroom/homepage.html', context)

@login_required(login_url='chatroom:login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    R_messages = room.message_set.all().order_by('created')
    context = {'room': room, 'R_messages':R_messages}
    return render(request, 'chatroom/room.html', context)

@login_required(login_url='chatroom:login')
def create_room(request):
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('chatroom:homepage')
    context = {'form': form}
    return render(request, 'chatroom/create_room.html', context)

@login_required(login_url='chatroom:login')
def update_room(request, pk):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    if request.user != room.host: #or request.user != superuser:
        return HttpResponse('you are not allow here!!')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('chatroom:homepage')
    context = {'form': form}
    return render(request, 'chatroom/create_room.html', context)

@login_required(login_url='chatroom:login')
def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('chatroom:homepage')
    context = {'room':room}
    return render(request, 'chatroom/delete_room.html', context)