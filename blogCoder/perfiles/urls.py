from django.urls import path
from perfiles.views import login_form
from django.contrib.auth.views import LogoutView

from perfiles.views import *

urlpatterns = [
    path('login/', login_form, name='login_form'),
    path('perfil', Perfil, name='perfil'),
    path('perfil/actualizar_usuario', actualizar_usuario, name='actualizar_usuario'),
    path('perfil/cargar_imagen/', cargar_avatar, name='cargar_imagen'),
    
    path('usuario/login/', login_form, name='login_form'),
    path('usuario/logout/', LogoutView.as_view(template_name='appblog/logout.html'), name='logout'),
    path('usuario/registro/', registro, name='registro'),

]
