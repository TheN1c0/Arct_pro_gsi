from django.shortcuts import render

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
