from django.shortcuts import render
from .models import FAQ, FreeCourse, PaidCourse, UpcomingCourse, Tutor
from chat.models import Room

free = FreeCourse.objects.all().count()
paid = PaidCourse.objects.all().count()
upcoming = UpcomingCourse.objects.all().count()
room = Room.objects.all().count()
tutor = Tutor.objects.all().count()

# Create your views here.
def homepage(request):
    page = 'home'
    questions = FAQ.objects.all()
    context = {'page': page, 'questions':questions, 'free': free, 'paid': paid, 'coming': upcoming, 'room': room, 'tutor': tutor}
    return render(request, 'home/homepage.html', context)

def not_found(request):
    return render(request, 'home/not_found.html')

def contact(request):
    context = {}
    return render(request, 'home/contact.html', context)