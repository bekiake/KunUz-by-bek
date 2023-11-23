from django import forms
from django.contrib.auth.forms import UserCreationForm  
from .models import User   

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name', 'phone', 'address','avatar', 'password1', 'password2']
        
        
        
class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'phone', 'address','avatar']