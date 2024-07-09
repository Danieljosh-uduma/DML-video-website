from django.forms import ModelForm
from .models import Room, Suggest

class RoomForm(ModelForm):
    
    class Meta:
        model = Room
        fields = '__all__'
        exclude = ['host', 'participants']
        
class SuggestForm(ModelForm):
    
    class Meta:
        model = Suggest
        fields = '__all__'
        exclude = ['host']