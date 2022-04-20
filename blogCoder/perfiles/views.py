
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from appblog.models import Avatar
from perfiles.forms import Usuario_registro
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm 
from django.contrib.auth import login, authenticate

from perfiles.forms import Usuario_editar, AvatarFormulario


# Create your views here.


def Perfil(request):
    
     if request.user.is_authenticated:
        avatar = Avatar.objects.filter(usuario = request.user)
    
        if len(avatar) > 0:
            imagen = avatar[0].img.url
            
            return render(request, 'perfiles/perfil.html', {'imagen': imagen})
        
        else:
            return render(request, 'perfiles/perfil.html')
            
    
@login_required(login_url='usuario/login/')
def actualizar_usuario(request):
    
    usuario = request.user

    
    if request.method == 'POST':
        form = Usuario_editar(request.POST)
        
        if form.is_valid():
            
            data = form.cleaned_data
            
            usuario.first_name = data['first_name']
            usuario.last_name = data['last_name']
            usuario.email = data['email']
            usuario.set_password(data['password1'])
            usuario.set_password(data['password2'])
            
            usuario.save()
            
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
            return redirect('login_form')
        else:
            return render(request, 'perfiles/registro.html', {'form': form, 'registraste': 'Formulario no válido'})
    else:
        form = Usuario_registro()
        return render(request, 'perfiles/registro.html', {'form': form})

#avatars
@login_required(login_url='login/')
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