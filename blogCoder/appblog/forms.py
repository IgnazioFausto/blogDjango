
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Nuevo_post(forms.Form):
    
    titulo = forms.CharField(max_length=60, widget=forms.TextInput(attrs={ 'placeholder': 'Título'}))
    contenido = forms.CharField(widget=forms.Textarea(attrs={ 'placeholder': 'Contenido'}))
        
        
        


