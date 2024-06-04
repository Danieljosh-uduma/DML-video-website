from django.shortcuts import render
from django.contrib.auth.models import User
from chat.models import Topic, Room, Message

# Create your views here.
def resource(request):
    page = 'resource'
    context = {'page':page}
    return render(request, 'user/resource.html', context)

def user_profile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    R_messages = user.message_set.all()
    topics = Topic.objects.all()
    context = {'user':user, 'rooms':rooms, 'R_messages': R_messages, 'topics':topics}
    return render(request, 'user/profile.html', context)