from django.urls import path
from . import views

urlpatterns = [

    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),  
    path('administracion_categorias/', views.administracion_categorias, name='administracion_categorias'),  
    path('administracion_pedidos/', views.administracion_pedidos, name='administracion_pedidos'),  
    path('inicio/', views.inicio, name='inicio'),  
    path('registrarse/', views.registrarse, name='registrarse'),  
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('productos_stock/', views.productos_stock, name='productos_stock'),  
    

]