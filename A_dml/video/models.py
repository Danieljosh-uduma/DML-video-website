from django.db import models
from home.models import Tutors
from chat.models import Topic
from embed_video.fields import EmbedVideoField

# Create your models here.
class Video(models.Model):
    name = models.CharField(max_length=50)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    tutor = models.ForeignKey(Tutors, on_delete=models.SET_NULL, null=True)
    url = EmbedVideoField()
    posted = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-posted', 'topic']
        
    def __str__(self):
        return str(self.name)