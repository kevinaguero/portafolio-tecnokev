from django.shortcuts import render

# Create your views here.

def cursos(request):
    #productos = Producto.objects.filter(vigencia=True)
    #data = {
    #    'productos': productos,
    #}

    return render(request, 'cursos/cursos.html')