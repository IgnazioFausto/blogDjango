from dataclasses import fields
from random import random
from django.shortcuts import render
from appblog.forms import Nuevo_post
from appblog.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView


# Views basadas en clases




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
      
        
    return render(request, 'appblog/nuevo_post.html', {'posteo': posteo, 'titulo': 'Nuevo post', 'cta': 'Publicar'})

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

def Post_random(request):
    
    if request.method == 'GET':
        posts = Posteos_nuevos.objects.all()
        post_random = posts[int(random()*len(posts))]
        
        return render(request, 'appblog/post.html', {'post': post_random})
        
def Eliminar_post(request, id):
    try:
        post = Posteos_nuevos.objects.get(id=id)
    
        post.delete()
        
    
        return render(request, 'appblog/inicio.html')
    except Exception as exc:
        return render(request, 'appblog/publicados.html')

def Editar_post(request, id):
   
    post_a_editar = Posteos_nuevos.objects.get(id=id)
    
    if request.method == 'POST':
        formulario_edicion = Nuevo_post(request.POST)
        if formulario_edicion.is_valid():
            
            data = formulario_edicion.cleaned_data
            
            post_a_editar.titulo = data['titulo']
            post_a_editar.post = data['contenido']
            
            post_a_editar.save()
            
            return render(request, 'appblog/post.html', {'post': post_a_editar})
    
    
    else: 
        
        
        formulario = Nuevo_post(initial={'titulo': post_a_editar.titulo, 'contenido': post_a_editar.post})
        
        return render(request, 'appblog/nuevo_post.html', {'posteo': formulario,'titulo': "Editando", 'cta': "Confirmar cambios"})

class Lista_post(ListView):
    
    model = Posteos_nuevos
    template_name = 'appblog/listado_post.html'

class Detalle_post(DetailView):
    
    model = Posteos_nuevos
    template_name = 'appblog/detalle_post.html'

class Crear_post(CreateView):
    
    model = Posteos_nuevos
    fields = ['titulo', 'post']
    success_url = '/posts/listado/'

class Actualizar_post(UpdateView):
    
    model = Posteos_nuevos
    fields = ['titulo', 'post']
    success_url = '/posts/listado/'

class Borrar_post(DeleteView):
    
    model = Posteos_nuevos
    template_name = 'appblog/confirm_borrar.html'
    success_url = '/posts/listado/'

