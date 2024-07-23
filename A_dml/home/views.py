from django.shortcuts import render, redirect
from .models import FAQ, FreeCourse, PaidCourse, UpcomingCourse, Tutor
from chat.models import Room
from .forms import ContactForm

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
    form = ContactForm
    
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home:homepage')
        
    context = {'form':form}
    return render(request, 'home/contact.html', context)

def services(request):
    return render(request, 'home/services.html')