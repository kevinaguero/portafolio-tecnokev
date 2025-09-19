from django.shortcuts import render
from apps.blog.models import Blog
from apps.curso.models import Curso
from apps.proyecto.models import Proyecto
from apps.configuraciones.models import Categoria, Novedad

# Create your views here.
def index_view(request):
    proyectos = Proyecto.objects.filter(vigencia=True)
    blogs = Blog.objects.filter(vigencia=True)
    cursos = Curso.objects.filter(vigencia=True)
    novedades = Novedad.objects.filter(vigencia=True)
    categorias = Categoria.objects.all()

    return render(request, 'index/index.html',{'proyectos': proyectos, 'blogs': blogs,
    'cursos': cursos, 'novedades':novedades,'categorias':categorias})