from django.urls import path
from appblog.views import *



urlpatterns = [
    #inicio
    path('', Inicio, name='inicio'),
    
    #login, logout, registro
    path('about/', Sobre_mi, name="sobre_mi"),
    
    #posteos, post, nuevo post, post random, editar post, eliminar post
    path('pages/', Publicados, name='publicados'),
    path('pages/<int:id>/', Post, name='post'),
    path('pages/new/', Nuevo_posteo, name='nuevo_post'),
    path('pages/random/', Post_random, name='post_random'),
    path('pages/edit/<int:id>/', Editar_post, name='editar_post'),
    path("pages/delete/<pk>/", Borrar_post.as_view(), name="eliminar_posts"),
    
  

]