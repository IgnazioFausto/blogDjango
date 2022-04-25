from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    
    usuario = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    web = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return str(self.usuario)
    