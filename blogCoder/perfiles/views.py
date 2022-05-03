
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from appblog.models import Avatar
from appblog.models import Posteos_nuevos
from perfiles.models import Mensajes
from perfiles.forms import Chats
from perfiles.models import Perfil
from perfiles.forms import Usuario_registro
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login, authenticate

from perfiles.forms import Usuario_editar, AvatarFormulario


# Create your views here.

@login_required(login_url='login_form')
def Perfiles(request):
    
    posts = Posteos_nuevos.objects.filter(autor_id = request.user.id)
    
    if request.user.is_authenticated:
        avatar = Avatar.objects.filter(usuario = request.user)
    
        if len(avatar) > 0:
            imagen = avatar[0].img.url
            
            return render(request, 'perfiles/perfil.html', {'imagen': imagen, 'posts': posts})
        
        else:
            return render(request, 'perfiles/perfil.html')
    
            
    
@login_required(login_url='login_form')
def actualizar_usuario(request):
    
    
    if request.method == 'POST':
        
        form = Usuario_editar(request.POST)
        
        
        if form.is_valid():
            
            data = form.cleaned_data
        
            
            
            perfil = Perfil.objects.get(usuario = request.user)
            
            perfil.nombre = data['first_name']
            perfil.apellido = data['last_name']
            perfil.email = data['email']
            perfil.bio = data['bio']
            perfil.web = data['web']
            
            perfil.save()
            
           
           
            
            return redirect('login_form')
        else: 
            return render(request, 'perfiles/actualizar_usuario.html', {'form': form, 'mensaje': 'Formulario no válido'})
    else:
        form = Usuario_editar(initial={'email': request.user.email, 'first_name': request.user.first_name, 'last_name': request.user.last_name})

        
        return render(request, 'perfiles/actualizar_usuario.html', {'form': form})
  
#login, registro
def login_form(request):
    
    if request.method == "POST":
        
        formulario = AuthenticationForm(data=request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            
            username = data['username']
            contrasenia = data['password']
            
            user = authenticate(username=username, password=contrasenia)
            
            if user is not None:
                login(request, user)
                if request.user.is_authenticated:
                    avatar = Avatar.objects.filter(usuario = request.user)
    
                    if len(avatar) > 0:
                        imagen = avatar[0].img.url
                        return render(request, 'appblog/inicio.html',{'imagen': imagen})
                    else:
                        return render(request, 'appblog/inicio.html')
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
            
          
            user = Perfil( usuario = form.save(), email = form.cleaned_data['email'])
            user.save()
            
            
            
            return redirect('login_form')
        else:
            return render(request, 'perfiles/registro.html', {'form': form, 'registraste': 'Formulario no válido'})
    else:
        form = Usuario_registro()
        return render(request, 'perfiles/registro.html', {'form': form})

#avatars
@login_required(login_url='login_form')
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
                avatar = Avatar(usuario = usuario, img = formulario.cleaned_data['imagen'])
                avatar.save()
        return redirect('inicio')
    else: 
        formulario = AvatarFormulario()
        return render(request, 'perfiles/cargar_imagen.html', {'form': formulario})
            
            
            
@login_required(login_url='login_form')
def Mensajeria(request):
    
    
        Usuarios = Perfil.objects.exclude(usuario = request.user)
        
        return render(request, 'perfiles/mensajeria.html', {'Usuarios': Usuarios})

@login_required(login_url='login_form')
def Chat(request, id):
    
    # chequeamos si el user esta autenticado para usar su avatar
    if request.user.is_authenticated:
        imagen = Avatar.objects.filter(usuario = request.user)
        if len(imagen) > 0:
            imagen = imagen[0].img.url
            
    
    # si se envia un mensaje
    if request.method == 'POST':
        
        form = Chats(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            # recogemos los datos del form para guardar el mensaje
            mensaje = Mensajes(emisor = request.user, destinatario = Perfil.objects.get(id = id), mensaje = data['mensaje'])
            mensaje.save()
            
            return redirect('chat', id)
        else:
            return render(request, 'perfiles/chat.html', {'form': form, 'mensaje': 'Formulario no válido'})
    else:
        
        form = Chats()
        nombre = Perfil.objects.get(id = id)
        
        #filtramos de la db los mensajes que sean del usuario actual y el destinatario
        mensajes_recibidos = Mensajes.objects.filter(destinatario = request.user.username).filter(emisor = nombre.usuario).order_by('-fecha')
        
        mensajes_enviados = Mensajes.objects.filter(emisor_id = request.user.id, destinatario = nombre).order_by('-fecha')[:8]
    
        
        # tomamos la imagen para el usuario al que se le manda mensaje
        imagen_chat = Avatar.objects.filter(usuario = nombre.usuario)
        if len(imagen_chat) > 0:
            imagen_chat = imagen_chat[0].img.url
        
        #retornamos con el dic necesario
        return render(request, 'perfiles/chat.html', {'id': id, 'form': form, 'nombre': nombre, 'mensajes_recibidos': mensajes_recibidos, 'mensajes_enviados': mensajes_enviados, 'imagen': imagen, 'imagen_chat': imagen_chat})