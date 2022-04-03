from django.urls import path
from appblog.views import *


urlpatterns = [
    path('', Inicio, name='inicio'),
    path('publicados/', Publicados, name='publicados'),
    path('publicados/<int:id>/', Post, name='post'),
    path('nuevo_post/', Nuevo_posteo, name='nuevo_post'),
    path('post_random/', Post_random, name='post_random'),
    path('eliminar_curso/<int:id>/', Eliminar_post, name='eliminar_post'),
    path('editar_post/<int:id>/', Editar_post, name='editar_post'),
    
    path("posts/listado/", Lista_post.as_view(), name="listado_posts"),
    path("post/crear/", Crear_post.as_view(), name="crear_post"),
    path("post/editar/<pk>",Actualizar_post.as_view(), name="editar_posts"),
    path("post/<pk>/", Detalle_post.as_view(), name="detalle_post"),
    path("post/eliminar/<pk>/", Borrar_post.as_view(), name="eliminar_posts"),

]