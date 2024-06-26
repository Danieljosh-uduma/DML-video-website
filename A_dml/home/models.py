from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class FAQs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)
    
    
class Tutors(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.name)
    
class FreeCourse(models.Model):
    topic = models.CharField(max_length=50)
    tutor = models.ForeignKey(Tutors, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.topic)
    
class PaidCourse(models.Model):
    topic = models.CharField(max_length=50)
    tutor = models.ForeignKey(Tutors, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.topic)
    
class UpcomingCourse(models.Model):
    topic = models.CharField(max_length=50)
    tutor = models.ForeignKey(Tutors, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.topic)