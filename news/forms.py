from django import forms
from .models import News

class AddNewForm(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'desc', 'body', 'img', 'video', 'category', 'tags', 'is_avtive']