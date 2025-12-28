from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

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

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, help_text="Foto de perfil del usuario")
    bio = models.TextField(blank=True, null=True, help_text="Biografía corta del autor")
    website = models.URLField(blank=True, null=True, help_text="Sitio web personal")
    github = models.CharField(max_length=100, blank=True, null=True, help_text="Usuario de GitHub")
    linkedin = models.CharField(max_length=100, blank=True, null=True, help_text="Usuario de LinkedIn")
    twitter = models.CharField(max_length=100, blank=True, null=True, help_text="Usuario de Twitter/X")

    class Meta:
        verbose_name = "Perfil de Usuario"
        verbose_name_plural = "Perfiles de Usuario"

    def save(self, *args, **kwargs):
        # Procesar avatar si existe y es nuevo
        if self.avatar and hasattr(self.avatar, 'file'):
            try:
                img = Image.open(self.avatar)
                
                # Convertir RGBA a RGB si es necesario
                if img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                
                # Dimensión para avatar: 400x400px (cuadrado)
                target_size = 400
                
                # Recortar al cuadrado desde el centro
                width, height = img.size
                if width > height:
                    left = (width - height) // 2
                    img = img.crop((left, 0, left + height, height))
                else:
                    top = (height - width) // 2
                    img = img.crop((0, top, width, top + width))
                
                # Redimensionar
                img = img.resize((target_size, target_size), Image.Resampling.LANCZOS)
                
                # Guardar
                output = BytesIO()
                img.save(output, format='JPEG', quality=95, optimize=True)
                output.seek(0)
                
                self.avatar = InMemoryUploadedFile(
                    output,
                    'ImageField',
                    f"{self.avatar.name.split('.')[0]}.jpg",
                    'image/jpeg',
                    sys.getsizeof(output),
                    None
                )
            except Exception as e:
                print(f"Error al procesar avatar: {e}")
        
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Perfil de {self.user.get_full_name() or self.user.username}"

# Signals para crear perfil automáticamente
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'profile'):
        instance.profile.save()
