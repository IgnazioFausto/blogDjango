from django.urls import path
from perfiles.views import login_form
from django.contrib.auth.views import LogoutView

from perfiles.views import *

urlpatterns = [
    #perfil
    path('accounts/profile', Perfiles, name='perfil'),
    #mensajeria
    path('messages/', Mensajeria, name='mensajeria'),
    path('chat/<id>', Chat, name='chat'),
    #editar perfil
    path('accounts/update_profile/', actualizar_usuario, name='actualizar_usuario'),
    path('accounts/upload_image/', cargar_avatar, name='cargar_imagen'),
    #registro, login y logout
    path('accounts/login/', login_form, name='login_form'),
    path('accounts/logout/', LogoutView.as_view(template_name='appblog/logout.html'), name='logout'),
    path('accounts/signup/', registro, name='registro'),

]
