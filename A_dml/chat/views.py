from django.shortcuts import render, redirect
from .models import Topic, Room, Message
from .forms import RoomForm, SuggestForm, MyRegisterForm
from user.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.

def login_page(request):
    page = 'login'
    
    if request.user.is_authenticated:
        return redirect('video:homepage')
    
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(email=email)
        except:
            messages.error(request, 'User does not exist!!')
            
        user = authenticate(request, email=email, password=password) 
         
        if user is not None:
            login(request, user)
            return redirect('home:homepage')
        else:
            messages.error(request, 'incorrect email or password')
        
    context= {'page':page}
    return render(request, 'chatroom/register.html', context)

def logout_page(request):
    logout(request)
    return redirect('home:homepage')

def register_page(request):
    if request.user.is_authenticated:
        return redirect('home:homepage')
    
    form = MyRegisterForm
    
    if request.method == 'POST':
        form = MyRegisterForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect('home:homepage')
        
    context = {'form': form}
    return render(request, 'chatroom/register.html', context)
    
@login_required(login_url='chatroom:login')
def homepage(request):
    page = 'chat'
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q)|
        Q(name__icontains=q)|
        Q(description__icontains=q)
    )
    room_count = rooms.count()
    topics = Topic.objects.all()[0:5]
    R_messages = Message.objects.filter(Q(room__topic__name__icontains=q))#.order_by('created')
    
    new_msg = []
    count = 0
    for msg in R_messages:
        count += 1
        new_msg.append(msg)
        if count == 10:
            break
        
    context = {'topics':topics, 'rooms':rooms, 'count':room_count, 'R_messages':R_messages, 'new_msg':new_msg, 'page':page}
    return render(request, 'chatroom/homepage.html', context)

@login_required(login_url='chatroom:login')
def room(request, pk):
    room = Room.objects.get(id=pk)
    R_messages = room.message_set.all().order_by('-created')
    participants = room.participants.all()
    
    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            body=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('chatroom:room', pk=room.id)
    num = participants.count()
    context = {'room': room, 'R_messages':R_messages, 'participants':participants, 'num':num}
    return render(request, 'chatroom/room.html', context)

@login_required(login_url='chatroom:login')
def create_room(request):
    page, pag = 'create', 'create'
    form = RoomForm
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user
            form.save()
            return redirect('chatroom:homepage')
    context = {'form': form, 'page':page,'pag':pag}
    return render(request, 'chatroom/create_room.html', context)

@login_required(login_url='chatroom:login')
def suggest_room(request):
    page = 'suggest'
    form = SuggestForm
    if request.method == 'POST':
        form = SuggestForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.host = request.user
            form.save()
            return redirect('chatroom:homepage')
    context = {'form': form, 'page':page}
    return render(request, 'chatroom/create_room.html', context)

@login_required(login_url='chatroom:login')
def update_room(request, pk):
    page = 'create'
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    
    #if request.user != room.host or request.user.is_superuser == False:
    #   return HttpResponse('you are not allow here!!')
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('chatroom:homepage')
    context = {'form': form, 'page':page}
    return render(request, 'chatroom/create_room.html', context)

@login_required(login_url='chatroom:login')
def delete_room(request,pk):
    room = Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('chatroom:homepage')
    context = {'obj':room}
    return render(request, 'chatroom/delete_room.html', context)

@login_required(login_url='chatroom:login')
def delete_message(request,pk):
    message = Message.objects.get(id=pk)
    
    if request.user != message.user:
       return HttpResponse('you are not allow here!!')
   
    if request.method == 'POST':
        message.delete()
        return redirect('chatroom:homepage')
    context = {'obj':message}
    return render(request, 'chatroom/delete_room.html', context)

@login_required(login_url='chatroom:login')
def topics(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(
        Q(name__icontains=q))
    
    topics_count = topics.count()
    
    context = {'topics':topics, 'count':topics_count}
    return render(request, 'chatroom/topics.html', context)

@login_required(login_url='chatroom:login')
def activities(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    R_messages = Message.objects.filter(Q(room__topic__name__icontains=q))[0:5]
    context = {'R_messages':R_messages}
    return render(request, 'chatroom/activity.html', context)