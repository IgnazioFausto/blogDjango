
from cProfile import label
import datetime
from tabnanny import verbose
from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm
from appblog.models import *
from ckeditor.widgets import CKEditorWidget

class Nuevo_post(forms.ModelForm):
    
    post = forms.CharField(widget=CKEditorWidget(), label='')
    fecha = forms.DateField(initial=datetime.datetime.today(), label='')
    class Meta:
        model = Posteos_nuevos
        fields = '__all__'
        labels = {
            'post': '',
        }
        
    
        
        
        


