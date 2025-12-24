from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from .models import Blog
from .forms import ComentarioForm
from django.contrib import messages
from apps.configuraciones.models import Categoria

# Create your views here.
def blog_view(request):
    blogs = Blog.objects.filter(vigencia=True)
    categorias = Categoria.objects.all()

    return render(request, 'blog/blog.html',{'blogs': blogs, 'categorias': categorias})


def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk)

    # ✅ Traer solo comentarios aprobados
    comentarios = blog.comentarios.filter(aprobado=True).order_by('-fecha')

    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            comentario = form.save(commit=False)
            comentario.blog = blog
            comentario.aprobado = False  # se aprueba desde el admin
            comentario.save()

            messages.success(request, "Tu comentario fue enviado y está en espera de aprobación.")
            return redirect('blog:blog_detail', pk=blog.pk)
    else:
        form = ComentarioForm()

    context = {
        'blog': blog,
        'comentarios': comentarios,
        'form': form,
    }
    return render(request, 'blog/blog_detalle.html', context)
