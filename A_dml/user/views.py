from django.shortcuts import render
from django.contrib.auth.models import User
from chat.models import Topic, Room, Message
from django.contrib.auth.decorators import login_required
from .forms import FormUser

# Create your views here.
@login_required(login_url='chatroom:login')
def resource(request):
    page = 'resource'
    rooms = Room.objects.all()
    context = {'page':page, 'rooms':rooms}
    return render(request, 'user/resource.html', context)

@login_required(login_url='chatroom:login')
def user_profile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    R_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user':user, 'rooms':rooms, 'R_messages': R_messages, 'topics':topics}
    return render(request, 'user/profile.html', context)

@login_required(login_url='chatroom:login')
def update_user(request):
    form = FormUser
    context = {'form': form}
    return render(request, 'user/update_user.html', context)
