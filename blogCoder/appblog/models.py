from django.db import models


# Create your models here.

class Posteos_nuevos(models.Model):
    
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=30)
    post = models.TextField(max_length=200)

