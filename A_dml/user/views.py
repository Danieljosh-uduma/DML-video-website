from django.shortcuts import render, redirect
from .models import User
from chat.models import Topic, Room, Suggest
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
    suggests = user.suggest_set.all()
    R_messages = user.message_set.all()
    topics = Topic.objects.all()[:5]
    context = {'user':user, 'rooms':rooms, 'R_messages': R_messages, 'topics':topics, 'suggests':suggests}
    return render(request, 'user/profile.html', context)

@login_required(login_url='chatroom:login')
def update_user(request):
    user = request.user
    form = FormUser(instance=user)
    context = {'form': form}
    
    if request.method == 'POST':
        form = FormUser(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user:profile', pk=user.id)
        
    return render(request, 'user/update_user.html', context)
