from random import random
from django.shortcuts import render, redirect
from appblog.forms import Nuevo_post
from appblog.models import *
from django.views.generic.edit import  DeleteView

#autenticacion django

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.

#inicio
def Inicio(request):
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(usuario = request.user)
    
        if len(avatar) > 0:
            imagen = avatar[0].img.url
    
            return render(request, 'appblog/inicio.html', {'imagen': imagen})
        else:
            return render(request, 'appblog/inicio.html')
    
    else:
        return render(request, 'appblog/inicio.html')

#posteos, post, nuevo post, post random, editar post, eliminar post  
def Publicados(request):
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(usuario = request.user)
    
        if len(avatar) > 0:
            imagen = avatar[0].img.url
        else:
            imagen = ''
    else:
        imagen = ''
    
    posts = Posteos_nuevos.objects.all().order_by('-fecha')
    
    if request.method == 'GET':
        buscar = request.GET.get('buscar')
        if buscar:
            posts = Posteos_nuevos.objects.filter(titulo__icontains=buscar)
            
    
    
    
    return render(request, 'appblog/publicados.html', {'posts': posts, 'imagen': imagen})

def Post(request, id):
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(usuario = request.user)
    
        if len(avatar) > 0:
            imagen = avatar[0].img.url
        else:
            imagen = ''
    else:
        imagen = ''
    
    post = Posteos_nuevos.objects.get(id=id)
    
    return render(request, 'appblog/post.html', {'post': post, 'imagen': imagen})

@login_required(login_url='/login/')
def Nuevo_posteo(request): 
    
    
    if request.method == 'POST':
        
        posteo = Nuevo_post(request.POST, request.FILES)
        if posteo.is_valid():
            
            data = posteo.cleaned_data
            
            post_nuevo = Posteos_nuevos(titulo=data['titulo'],img=data['img'], post=data['post'], fecha=data['fecha'], autor=request.user)
   
            post_nuevo.save()
            
            
            
            return redirect('/posts/publicados/{}'.format(post_nuevo.id))
        else:
            return render(request, 'appblog/nuevo_post.html', {'form': posteo, 'error': 'Formulario no válido'})
    else:
        posteo = Nuevo_post()
      
        
        return render(request, 'appblog/nuevo_post.html', {'posteo': posteo, 'titulo': 'Escribir post', 'cta': 'Publicar'})

def Post_random(request):
    
    
    if request.method == 'GET':
        posts = Posteos_nuevos.objects.all()
        if len(posts) > 0:
            post = posts[int(random()*len(posts))]
            return redirect('/posts/publicados/{}'.format(post.id))
        else:
            if request.user.is_authenticated:
                avatar = Avatar.objects.filter(usuario = request.user)
    
                if len(avatar) > 0:
                    imagen = avatar[0].img.url
                    return render(request, 'appblog/inicio.html', {'aviso': 'No hay posts para mostrar. Ingresa y publica uno!', 'imagen': imagen})
                else:
                    imagen = ''
            else:
                return render(request, 'appblog/inicio.html', {'aviso': 'No hay posts para mostrar. Ingresa y publica uno!'})
        
@login_required(login_url='/login/')
def Editar_post(request, id):
   
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(usuario = request.user)
    
        if len(avatar) > 0:
            imagen = avatar[0].img.url
        else:
            imagen = ''
            
        
    post_a_editar = Posteos_nuevos.objects.get(id=id)
    
    if request.method == 'POST':
        formulario_edicion = Nuevo_post(request.POST, request.FILES, instance=post_a_editar)
        if formulario_edicion.is_valid():
            
            data = formulario_edicion.cleaned_data
            
            post_a_editar.titulo = data['titulo']
            post_a_editar.post = data['post']
            
            post_a_editar.save()
            
            return render(request, 'appblog/post.html', {'post': post_a_editar, 'imagen': imagen})
    
    
    else: 
        
        
        formulario = Nuevo_post(initial={'titulo': post_a_editar.titulo, 'post': post_a_editar.post, 'img': post_a_editar.img})
        
        return render(request, 'appblog/nuevo_post.html', {'posteo': formulario,'titulo': "Editar", 'cta': "Confirmar cambios", 'imagen': imagen})

class Borrar_post(LoginRequiredMixin, DeleteView):
    
    model = Posteos_nuevos
    template_name = 'appblog/confirm_borrar.html'
    success_url = '/posts/publicados/'


def Sobre_mi(request):
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(usuario = request.user)
    
        if len(avatar) > 0:
            imagen = avatar[0].img.url
        else:
            imagen = ''
    
        return render(request, 'appblog/sobre_mi.html', {'imagen': imagen})
    else:
        return render(request, 'appblog/sobre_mi.html')