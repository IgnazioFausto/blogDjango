from django.db import models


# Create your models here.

class Posteos_nuevos(models.Model):
    
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    post = models.TextField(max_length=200)
    
    def __str__(self) -> str:
        return f"Título: {self.titulo}"

class Post_random(models.Model):
    
    id = models.IntegerField(primary_key=True)
    