from django.db import models
from apps.configuraciones.models import Categoria

# Create your models here.

class Curso(models.Model):
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='cursos/')
    categorias = models.ManyToManyField(Categoria, blank=True)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
