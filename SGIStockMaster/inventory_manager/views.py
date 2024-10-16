from django.shortcuts import render

# Create your views here.
def agregar_producto(request):
    return render(request, 'inventory_manager/SGI_agregar_producto.html')

def administracion_categorias(request):
    return render(request, 'inventory_manager/SGI_administracion_categorias.html')

def administracion_pedidos(request):
    return render(request, 'inventory_manager/SGI_administracion_pedidos.html')
