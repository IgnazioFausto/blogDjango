from random import random
from django.shortcuts import render, redirect
from appblog.forms import Nuevo_post, Usuario_registro
from appblog.models import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

#autenticacion django
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.

def Inicio(request):
    return render(request, 'appblog/inicio.html')

@login_required(login_url='/login/')
def Nuevo_posteo(request):
    
    if request.method == 'POST':
        
        posteo = Nuevo_post(request.POST)
        if posteo.is_valid():
            
            data = posteo.cleaned_data
            
            post_nuevo = Posteos_nuevos(titulo=data['titulo'], post=data['contenido'])
 
            post_nuevo.save()
            
            
            
            return redirect('/publicados/{}'.format(post_nuevo.id))
        else:
            return render(request, 'appblog/nuevo_post.html', {'form': posteo, 'error': 'Formulario no válido'})
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
        if len(posts) > 0:
            post = posts[int(random()*len(posts))]
            return render(request, 'appblog/post.html', {'post': post, 'mensaje': ''})
        else:
            return render(request, 'appblog/inicio.html', {'aviso': 'No hay posts para mostrar. Ingresa y publica uno!'})
        
        

@login_required(login_url='/login/')
def Eliminar_post(request, id):
    try:
        post = Posteos_nuevos.objects.get(id=id)
    
        post.delete()
        
    
        return redirect('/publicados/')
    except Exception as exc:
        return render(request, 'appblog/publicados.html')

@login_required(login_url='/login/')
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


# Views basadas en clases
class Lista_post(ListView):
    
    model = Posteos_nuevos
    template_name = 'appblog/listado_post.html'

class Detalle_post(DetailView):
    
    model = Posteos_nuevos
    template_name = 'appblog/detalle_post.html'

class Crear_post(LoginRequiredMixin, CreateView):
    
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

def login_form(request):
    
    if request.method == "POST":
        
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            username = data['username']
            contrasenia = data['password']
            
            user = authenticate(username=username, password=contrasenia)
            
            if user is not None:
                login(request, user)
                return render(request, 'appblog/inicio.html', {'mensaje': username})
            else:
                return render(request, 'appblog/login.html', {'form': formulario, 'mensaje': 'Usuario o contraseña incorrectos'})
        else:
            return render(request, 'appblog/login.html', {'form': formulario, 'mensaje': 'Formulario no válido'})
    else:
        form = AuthenticationForm()
        return render(request, 'appblog/login.html', {'form': form})

def registro(request):
    
    if request.method == "POST":
        form = Usuario_registro(request.POST)
        
        if form.is_valid():
            usuario = form.cleaned_data['username']
            
            
            form.save()
            return render(request, 'appblog/inicio.html', {'mensaje': usuario})
        else:
            return render(request, 'appblog/registro.html', {'form': form, 'mensaje': 'Formulario no válido'})
    else:
        form = Usuario_registro()
        return render(request, 'appblog/registro.html', {'form': form})
        
        
        