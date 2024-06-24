from django.db import models

# Create your models here.
class FAQs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=600)
    created = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.title)