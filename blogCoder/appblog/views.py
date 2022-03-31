from django.shortcuts import render
from appblog.forms import Nuevo_post
from appblog.models import *


# Create your views here.

def Inicio(request):
    return render(request, 'appblog/inicio.html')


def Nuevo_posteo(request):
    
    if request.method == 'POST':
        
        posteo = Nuevo_post(request.POST)
        if posteo.is_valid():
            
            data = posteo.cleaned_data
            
            post_nuevo = Posteos_nuevos(titulo=data['titulo'], post=data['contenido'])
 
            post_nuevo.save()
            
            posteo = Nuevo_post()
            
            return render(request, "appblog/publicados.html")      
    else:
        posteo = Nuevo_post()
      
        
    return render(request, 'appblog/nuevo_post.html', {'posteo': posteo})



def Publicados(request):
    
    posts = Posteos_nuevos.objects.all()
    
    if request.method == 'GET':
        buscar = request.GET.get('buscar')
        if buscar:
            posts = Posteos_nuevos.objects.filter(titulo__icontains=buscar)
    
    
    
    return render(request, 'appblog/publicados.html', {'posts': posts})

def Post(request, id):
    
    post = Posteos_nuevos.objects.get(id=id)
    
    return render(request, 'appblog/post.html', {'post': post})



    

