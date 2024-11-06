from django.urls import path
from . import views

urlpatterns = [

    path('agregar-producto/', views.agregar_producto, name='agregar_producto'),  
    path('administracion_categorias/', views.administracion_categorias, name='administracion_categorias'),  
    path('administracion_pedidos/', views.administracion_pedidos, name='administracion_pedidos'),
    path('administracion_productos/', views.administracion_productos, name='administracion_productos'),
    path('inicio/', views.inicio, name='inicio'),  
    path('registrarse/', views.registrarse, name='registrarse'),  
    path('dashboard/', views.dashboard, name='dashboard'),  
    path('productos_stock/', views.productos_stock, name='productos_stock'),  
    path('home/', views.homee, name='home'),
    path('recuperar_contrasena/', views.recuperar_contrasena, name='recuperar_contrasena'),
    path('restablecer_contrasena/<str:uidb64>/<str:token>/', views.restablecer_contrasena, name='restablecer_contrasena'),
    path('SGI_colaborador_dashboard/', views.colaborador_dashboard, name='colaborador_dashboard'),
    path('ver_pedidos/', views.ver_pedidos, name='ver_pedidos'),
    path('control_de_stock/', views.control_de_stock, name='control_de_stock')
    
    
]