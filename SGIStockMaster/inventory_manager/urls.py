from django.urls import path
from . import views

urlpatterns = [
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),
    path('crear-categoria/', views.crear_categoria, name='crear_categoria'),
]