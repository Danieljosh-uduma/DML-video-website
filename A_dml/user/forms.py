from django.forms import ModelForm
from .models import User

class FormUser(ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'bio', 'username', 'email']
    
