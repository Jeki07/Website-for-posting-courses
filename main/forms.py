from .models import Post
from django.forms import ModelForm, TextInput, FileInput, Textarea
from django import forms



class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'anons', 'image', 'video']
        
        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': "Названия запися"
            }),
            'anons': Textarea(attrs={
                'class': 'form-control',
                'placeholder': "Текст запися"
            }),
            'image': FileInput(attrs={
                
            }),
            'video': FileInput(attrs={
            }),
            
        }
            