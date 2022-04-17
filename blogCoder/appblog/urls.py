from django.urls import path
from appblog.views import *



urlpatterns = [
    #inicio
    path('', Inicio, name='inicio'),
    
    #login, logout, registro
    path('about/', Sobre_mi, name="sobre_mi"),
    
    #posteos, post, nuevo post, post random, editar post, eliminar post
    path('posts/publicados/', Publicados, name='publicados'),
    path('posts/publicados/<int:id>/', Post, name='post'),
    path('posts/nuevo/', Nuevo_posteo, name='nuevo_post'),
    path('post_random/', Post_random, name='post_random'),
    path('editar_post/<int:id>/', Editar_post, name='editar_post'),
    path("posts/eliminar/<pk>/", Borrar_post.as_view(), name="eliminar_posts"),
    
  

]