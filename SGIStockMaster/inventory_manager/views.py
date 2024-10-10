from django.shortcuts import render

# Create your views here.

def agregar_producto(request):
    return render(request, 'inventory_manager/SGI_agregar_producto.html')

def crear_categoria(request):
    return render(request, 'inventory_manager/SGI_crear_categoria.html')