from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Perfil(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    bio = models.TextField(max_length=500, null=True, blank=True)
    web = models.URLField(max_length=200, null=True, blank=True)
    
    def __str__(self):
        return self.usuario.username
    