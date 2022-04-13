from django.urls import path
from appblog.views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    #inicio
    path('', Inicio, name='inicio'),
    
    #login, logout, registro
    path('usuario/login/', login_form, name='login_form'),
    path('usuario/logout/', LogoutView.as_view(template_name='appblog/logout.html'), name='logout'),
    path('usuario/registro/', registro, name='registro'),
    path('usuario/actualizar/', actualizar_usuario, name='actualizar_usuario'),
    
    #posteos, post, nuevo post, post random, editar post, eliminar post
    path('posts/publicados/', Publicados, name='publicados'),
    path('posts/publicados/<int:id>/', Post, name='post'),
    path('posts/nuevo/', Nuevo_posteo, name='nuevo_post'),
    path('post_random/', Post_random, name='post_random'),
    path('editar_post/<int:id>/', Editar_post, name='editar_post'),
    path("posts/eliminar/<pk>/", Borrar_post.as_view(), name="eliminar_posts"),
    
    path('cargar_imagen/', cargar_avatar, name='cargar_imagen'),

]