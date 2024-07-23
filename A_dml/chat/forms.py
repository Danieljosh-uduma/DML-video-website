from django.forms import ModelForm
from .models import Room, Suggest
from user.models import User
from django.contrib.auth.forms import UserCreationForm


class MyRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['name', 'username', 'email', 'password1', 'password2'] 
        
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