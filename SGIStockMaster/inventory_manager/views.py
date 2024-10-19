from django.shortcuts import render
import requests

# Create your views here.
def agregar_producto(request):
    return render(request, 'inventory_manager/SGI_agregar_producto.html')

def administracion_categorias(request):
    return render(request, 'inventory_manager/SGI_administracion_categorias.html')

def administracion_pedidos(request):
    return render(request, 'inventory_manager/SGI_administracion_pedidos.html')

def inicio(request):
    return render(request, 'inventory_manager/SGI_inicio.html')

def registrarse(request):
    return render(request, 'inventory_manager/SGI_registrarse.html')

def dashboard(request):
    return render(request, 'inventory_manager/SGI_dashboard.html')

import requests
from django.shortcuts import render

def homee(request):
    # URL de la API (ajústala según tu configuración)
    categorias_url = 'http://127.0.0.1:8001/api/categorias/'
    productos_url = 'http://127.0.0.1:8001/api/productos/'

    # Realiza las solicitudes GET a la API
    categorias_response = requests.get(categorias_url)
    productos_response = requests.get(productos_url)

    # Verifica que la respuesta sea exitosa (código 200)
    if categorias_response.status_code == 200 and productos_response.status_code == 200:
        categorias_data = categorias_response.json().get('categorias', [])
        productos_data = productos_response.json().get('productos', [])

        # Crear un diccionario para organizar los productos por categoría
        categorias_con_productos = {}
        for categoria in categorias_data:
            categorias_con_productos[categoria['idCategoria']] = {
                'nombre': categoria['nombre'],
                'descripcion': categoria['descripcion'],
                'productos': []
            }

        # Agrupar productos por categoría
        for producto in productos_data:
            categoria_id = producto['categoria']  # ID de la categoría a la que pertenece el producto
            if categoria_id in categorias_con_productos:
                categorias_con_productos[categoria_id]['productos'].append(producto)

        # Enviar los datos al template
        context = {
            'categorias': categorias_con_productos
        }
        return render(request, 'inventory_manager/SGI_home.html', context)
    else:
        context = {
            'error': 'No se pudieron cargar los datos de las categorías y productos'
        }
        return render(request, 'inventory_manager/SGI_home.html', context)
