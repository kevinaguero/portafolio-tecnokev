from django.db import models
from apps.configuraciones.models import Categoria

# Create your models here.

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    contenido = RichTextField()  # contenido formateado
    imagen = models.ImageField(upload_to='blog/')
    categorias = models.ManyToManyField(Categoria, blank=True)
    vigencia = models.BooleanField(default=True)
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.titulo

class Comentario(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comentarios')
    autor = models.CharField(max_length=100)
    email = models.EmailField()
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    aprobado = models.BooleanField(default=False)  # aprobar manualmente antes de mostrar

    def __str__(self):
        return f"Comentario de {self.autor} en {self.blog.titulo}"
