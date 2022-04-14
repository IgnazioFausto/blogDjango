from random import random
from re import A
from django.shortcuts import render, redirect
from appblog.forms import Nuevo_post, Usuario_registro, Usuario_editar, AvatarFormulario
from appblog.models import *
from django.views.generic.edit import  DeleteView

#autenticacion django
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login, logout, authenticate
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

#login, registro
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
                return redirect('inicio')
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
            return redirect('/inicio/')
        else:
            return render(request, 'appblog/registro.html', {'form': form, 'registraste': 'Formulario no válido'})
    else:
        form = Usuario_registro()
        return render(request, 'appblog/registro.html', {'form': form})
        
@login_required(login_url='/usuario/login/')
def actualizar_usuario(request):
    
    usuario = request.user

    
    if request.method == 'POST':
        form = Usuario_editar(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
     
            usuario.email = data['email']
            usuario.set_password(data['password1'])
            usuario.set_password(data['password2'])
            
            usuario.save()
            
            return redirect('inicio')
        else: 
            return render(request, 'appblog/actualizar_usuario.html', {'form': form, 'mensaje': 'Formulario no válido'})
    else:
        form = Usuario_editar(initial={'email': request.user.email})

        
        return render(request, 'appblog/actualizar_usuario.html', {'form': form})
  

#posteos, post, nuevo post, post random, editar post, eliminar post  
def Publicados(request):
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(usuario = request.user)
    
        if len(avatar) > 0:
            imagen = avatar[0].img.url
    else:
        imagen = ''
    
    posts = Posteos_nuevos.objects.all()
    
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
    
    post = Posteos_nuevos.objects.get(id=id)
    
    return render(request, 'appblog/post.html', {'post': post, 'imagen': imagen})

@login_required(login_url='/login/')
def Nuevo_posteo(request):
    
    
    if request.method == 'POST':
        
        posteo = Nuevo_post(request.POST)
        if posteo.is_valid():
            
            data = posteo.cleaned_data
            
            post_nuevo = Posteos_nuevos(titulo=data['titulo'], post=data['contenido'])
   
            post_nuevo.save()
            
            
            
            return redirect('/posts/publicados/{}'.format(post_nuevo.id))
        else:
            return render(request, 'appblog/nuevo_post.html', {'form': posteo, 'error': 'Formulario no válido'})
    else:
        posteo = Nuevo_post()
      
        
    return render(request, 'appblog/nuevo_post.html', {'posteo': posteo, 'titulo': 'Escribir post', 'cta': 'Publicar'})

def Post_random(request):
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(usuario = request.user)
    
        if len(avatar) > 0:
            imagen = avatar[0].img.url
    
    if request.method == 'GET':
        posts = Posteos_nuevos.objects.all()
        if len(posts) > 0:
            post = posts[int(random()*len(posts))]
            return redirect('/posts/publicados/{}'.format(post.id))
        else:
            return render(request, 'appblog/inicio.html', {'aviso': 'No hay posts para mostrar. Ingresa y publica uno!', 'imagen': imagen})
        

@login_required(login_url='/login/')
def Editar_post(request, id):
   
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(usuario = request.user)
    
        if len(avatar) > 0:
            imagen = avatar[0].img.url
            
        
    post_a_editar = Posteos_nuevos.objects.get(id=id)
    
    if request.method == 'POST':
        formulario_edicion = Nuevo_post(request.POST)
        if formulario_edicion.is_valid():
            
            data = formulario_edicion.cleaned_data
            
            post_a_editar.titulo = data['titulo']
            post_a_editar.post = data['contenido']
            
            post_a_editar.save()
            
            return render(request, 'appblog/post.html', {'post': post_a_editar, 'imagen': imagen})
    
    
    else: 
        
        
        formulario = Nuevo_post(initial={'titulo': post_a_editar.titulo, 'contenido': post_a_editar.post})
        
        return render(request, 'appblog/nuevo_post.html', {'posteo': formulario,'titulo': "Editar", 'cta': "Confirmar cambios", 'imagen': imagen})

class Borrar_post(LoginRequiredMixin, DeleteView):
    
    model = Posteos_nuevos
    template_name = 'appblog/confirm_borrar.html'
    success_url = '/posts/publicados/'


#avatars
@login_required(login_url='/login/')
def cargar_avatar(request):
    
    if request.method == 'POST':
        formulario = AvatarFormulario(request.POST, request.FILES)
        
        if formulario.is_valid():
            usuario = request.user
            avatar = Avatar.objects.filter(usuario = usuario)
            
            if len(avatar) > 0:
                avatar = avatar[0]
                avatar.img = formulario.cleaned_data['imagen']
                avatar.save()
            else:
                avatar = Avatar(user = usuario, img = formulario.cleaned_data['imagen'])
                avatar.save()
        return redirect('inicio')
    else: 
        formulario = AvatarFormulario()
        return render(request, 'appblog/cargar_imagen.html', {'form': formulario})


