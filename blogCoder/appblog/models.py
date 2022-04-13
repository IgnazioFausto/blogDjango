from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Posteos_nuevos(models.Model):
    
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=60)
    post = models.TextField()
    
    def __str__(self) -> str:
        return f"Título: {self.titulo}"

class Post_random(models.Model):
    
    id = models.IntegerField(primary_key=True)
    
    
    
class Avatar(models.Model):
    
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    img = models.ImageField(upload_to='avatar/', null=True, blank=True)
   