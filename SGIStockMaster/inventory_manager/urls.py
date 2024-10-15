from django.urls import path
from . import views

urlpatterns = [
    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),  
    path('administracion_categorias/', views.administracion_categorias, name='administracion_categorias'),  
    
]