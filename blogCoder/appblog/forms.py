from dataclasses import fields
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm

class Nuevo_post(forms.Form):
    

    titulo = forms.CharField(max_length=30)
    contenido = forms.CharField(max_length=200)
    
class Usuario_registro(UserCreationForm):
    
    
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput, )
    password2 = forms.CharField(label="Contraseña2",widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = { k:"" for k in fields }
        
        
    