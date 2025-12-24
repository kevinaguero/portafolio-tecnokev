from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nombre

class Carousel(models.Model):
    titulo = models.CharField(max_length=200, help_text="Título principal del carousel")
    descripcion = models.TextField(help_text="Descripción o subtítulo")
    imagen = models.ImageField(upload_to='carousel/', help_text="Imagen de fondo del carousel")
    categorias = models.ManyToManyField(Categoria, blank=True, help_text="Categorías relacionadas (opcional)")
    nombre_boton = models.CharField(max_length=100, blank=True, null=True, help_text="Texto del botón (opcional)")
    link_boton = models.URLField(blank=True, null=True, help_text="URL del botón (opcional)")
    orden = models.IntegerField(default=0, help_text="Orden de aparición (menor número = primero)")
    vigencia = models.BooleanField(default=True, help_text="Si está activo o no")
    fecha_creacion = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['orden', '-fecha_creacion']
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousels'

    def __str__(self):
        return f"{self.orden} - {self.titulo}"
