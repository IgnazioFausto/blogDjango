from django import forms

class Nuevo_post(forms.Form):
    

    titulo = forms.CharField(max_length=30)
    contenido = forms.CharField(max_length=200)