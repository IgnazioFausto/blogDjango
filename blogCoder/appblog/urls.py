from django.urls import path
from appblog.views import *


urlpatterns = [
    path('', Inicio, name='inicio'),
    path('publicados/', Publicados, name='publicados'),
    path('publicados/<int:id>/', Post, name='post'),
    path('nuevo_post/', Nuevo_posteo, name='nuevo_post'),

]