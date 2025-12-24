from django.shortcuts import render
from .models import Proyecto
from apps.configuraciones.models import Categoria

# Create your views here.
def proyectos_view(request):
    proyectos = Proyecto.objects.filter(vigencia=True)
    categorias = Categoria.objects.all()

    return render(request, 'proyectos/proyectos.html', {'proyectos': proyectos, 'categorias': categorias})