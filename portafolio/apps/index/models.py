from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class AboutSection(models.Model):
    """Modelo para la sección 'Acerca de mí'"""
    TIPO_CHOICES = [
        ('principal', 'Card Principal (con avatar)'),
        ('secundaria', 'Card Secundaria'),
    ]
    
    tipo = models.CharField(max_length=20, choices=TIPO_CHOICES, default='secundaria', help_text="La card principal siempre se muestra primero con el avatar")
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(help_text="Contenido principal de la card")
    orden = models.IntegerField(default=0, help_text="Orden de visualización (menor número = primero)")
    vigencia = models.BooleanField(default=True)
    icono = models.CharField(max_length=100, blank=True, null=True, help_text="Clase de icono Font Awesome (ej: fa-solid fa-briefcase)")
    
    # Campos específicos para card principal
    avatar = models.ImageField(upload_to='about/', blank=True, null=True, help_text="Solo para card principal")
    usuario = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="Usuario asociado (opcional)")
    
    class Meta:
        ordering = ['orden']
        verbose_name = "Sección Acerca de Mí"
        verbose_name_plural = "Secciones Acerca de Mí"
    
    def __str__(self):
        return f"{self.get_tipo_display()} - {self.titulo}"
    
    def save(self, *args, **kwargs):
        # Asegurar que solo haya una card principal activa
        if self.tipo == 'principal' and self.vigencia:
            AboutSection.objects.filter(tipo='principal', vigencia=True).exclude(pk=self.pk).update(vigencia=False)
        super().save(*args, **kwargs)


class AboutBadge(models.Model):
    """Modelo para los badges de tecnologías en la card principal"""
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='badges', limit_choices_to={'tipo': 'principal'})
    nombre = models.CharField(max_length=50, help_text="Nombre de la tecnología")
    icono = models.CharField(max_length=100, blank=True, null=True, help_text="Clase de icono Font Awesome o URL de imagen")
    icono_tipo = models.CharField(max_length=20, choices=[('fontawesome', 'Font Awesome'), ('url', 'URL de imagen')], default='fontawesome')
    orden = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['orden']
        verbose_name = "Badge de Tecnología"
        verbose_name_plural = "Badges de Tecnologías"
    
    def __str__(self):
        return self.nombre


class AboutListItem(models.Model):
    """Modelo para items de lista en cards secundarias"""
    about_section = models.ForeignKey(AboutSection, on_delete=models.CASCADE, related_name='list_items', limit_choices_to={'tipo': 'secundaria'})
    texto = models.CharField(max_length=200)
    orden = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['orden']
        verbose_name = "Item de Lista"
        verbose_name_plural = "Items de Lista"
    
    def __str__(self):
        return self.texto
