from django.db import models
from user.models import User
from chat.models import Topic

# Create your models here.
class FAQ(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)
    
    
class Tutor(models.Model):
    name = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return str(self.name)
    
class FreeCourse(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.topic)
    
class PaidCourse(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.topic)
    
class UpcomingCourse(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.topic)