from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre
    
class Novedad(models.Model):
    titulo = models.CharField(max_length=200)
    tags = models.CharField(max_length=200, blank=True)  # etiquetas separadas por comas
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to='novedades/')
    link = models.URLField(blank=True, null=True)
    vigencia = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo
