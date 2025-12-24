from django.shortcuts import render
from apps.blog.models import Blog
from apps.curso.models import Curso
from apps.proyecto.models import Proyecto
from apps.configuraciones.models import Categoria, Novedad, Carousel

# Create your views here.
def index_view(request):
    proyectos = Proyecto.objects.filter(vigencia=True)
    blogs = Blog.objects.filter(vigencia=True)
    cursos = Curso.objects.filter(vigencia=True)
    novedades = Novedad.objects.filter(vigencia=True)
    carousels = Carousel.objects.filter(vigencia=True)
    
    # Categorías relacionadas con proyectos
    categorias_proyectos = Categoria.objects.filter(proyecto__isnull=False).distinct()

    # Categorías relacionadas con blogs
    categorias_blogs = Categoria.objects.filter(blog__isnull=False).distinct()

    return render(request, 'index/index.html',{
        'proyectos': proyectos, 
        'blogs': blogs,
        'cursos': cursos, 
        'novedades': novedades,
        'carousels': carousels,
        'categorias_proyectos': categorias_proyectos,
        'categorias_blogs': categorias_blogs,
    })