from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



#actualizar_usuario
class Usuario_registro(UserCreationForm):
    
    
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput, )
    password2 = forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = { k:"" for k in fields }
        
        
        
        
class Usuario_editar(UserCreationForm):
    

    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña",widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']
        help_texts = { k:"" for k in fields }  
        
    
class AvatarFormulario(forms.Form):
    
    imagen = forms.ImageField()