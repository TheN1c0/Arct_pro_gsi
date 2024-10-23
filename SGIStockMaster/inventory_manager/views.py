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
def productos_stock(request):
    return render(request, 'inventory_manager/SGI_productos_stock.html')

def administracion_productos(request):
    return render(request, 'inventory_manager/SGI_administracion_productos.html')

def recuperar_contrasena(request):
    return render(request, 'inventory_manager/SGI_recuperar_contrasena.html')


from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.utils.http import urlsafe_base64_decode


import logging

logger = logging.getLogger(__name__)
def restablecer_contrasena(request, uidb64, token):
    uid = urlsafe_base64_decode(uidb64).decode()

    if True:  # Cambia esto por tu validación real de token
        if request.method == 'POST':
            nueva_contrasena = request.POST.get('password')
            #creo que falta colocar bien el email
            if nueva_contrasena:
                url_api = f"http://127.0.0.1:8001/api/cambiar_contrasena/{uid}/"
                headers = {
                    'Content-Type': 'application/json',
                    'Authorization': 'Token <token_del_usuario>'  # Cambia esto por el token real
                }

                data = {'password': nueva_contrasena}
                
                try:
                    response = requests.post(url_api, headers=headers, json=data)
                    logger.info(f'Respuesta de la API: {response.status_code} - {response.json()}')

                    if response.status_code == 200:
                        # Aquí obtendremos nuevos tokens después de cambiar la contraseña
                        # Suponiendo que el usuario se puede autenticar de nuevo con su email y nueva contraseña
                        credentials = {
                            'email': response.json().get('email'),  # Asegúrate de que esto esté disponible en la respuesta
                            'password': nueva_contrasena
                        }
                        
                        # Obtén los nuevos tokens
                        token_api_url = "http://127.0.0.1:8001/api/token/"  # Cambia esto si es necesario
                        token_response = requests.post(token_api_url, json=credentials)

                        if token_response.status_code == 200:
                            tokens = token_response.json()
                            messages.success(request, "Contraseña cambiada y token actualizado con éxito.")
                            return JsonResponse({
                                'success': 'Contraseña cambiada con éxito.',
                                'access': tokens['access'],
                                'refresh': tokens['refresh']
                            }, status=200)
                        else:
                            error_message = token_response.json().get('error', 'Error al obtener nuevos tokens.')
                            return JsonResponse({'error': error_message}, status=token_response.status_code)

                    else:
                        error_message = response.json().get('error', 'Error desconocido al cambiar la contraseña.')
                        return JsonResponse({'error': error_message}, status=response.status_code)

                except requests.exceptions.RequestException as e:
                    logger.error(f'Error de conexión a la API: {str(e)}')
                    return JsonResponse({'error': 'Error de conexión a la API.',
                                         'contraseña': nueva_contrasena,
                                         'uid': uid}, status=500)

            else:
                return JsonResponse({'error': 'La contraseña no puede estar vacía.'}, status=400)
        else:
            return render(request, 'inventory_manager/SGI_restablecer_contrasena.html', {'uidb64': uidb64, 'token': token})
    else:
        return JsonResponse({'error': 'Token no válido o expirado'}, status=400)







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
