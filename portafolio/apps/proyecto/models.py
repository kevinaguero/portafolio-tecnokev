from django.db import models
from apps.configuraciones.models import Categoria
# Create your models here.

class Proyecto(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='proyectos/')
    categorias = models.ManyToManyField(Categoria, blank=True)
    titulo_boton = models.CharField(max_length=50, blank=True)
    link_boton = models.URLField(blank=True, null=True)
    link_github = models.URLField(blank=True, null=True)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
