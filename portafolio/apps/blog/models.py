from django.db import models
from apps.configuraciones.models import Categoria

# Create your models here.

from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.utils.text import slugify
from PIL import Image
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
import sys

class Blog(models.Model):
    titulo = models.CharField(max_length=200)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    descripcion = models.TextField()
    contenido = RichTextField()  # contenido formateado
    imagen = models.ImageField(upload_to='blog/')
    imagen_epigrafe = models.CharField(max_length=300, blank=True, null=True, help_text="Descripción o epígrafe de la imagen destacada")
    categorias = models.ManyToManyField(Categoria, blank=True)
    vigencia = models.BooleanField(default=True)
    fecha = models.DateField(auto_now_add=True)
    autor = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.titulo)
        
        # Procesar imagen si es nueva o cambió
        if self.imagen and hasattr(self.imagen, 'file'):
            try:
                img = Image.open(self.imagen)
                
                # Convertir RGBA a RGB si es necesario
                if img.mode in ('RGBA', 'LA', 'P'):
                    background = Image.new('RGB', img.size, (255, 255, 255))
                    if img.mode == 'P':
                        img = img.convert('RGBA')
                    background.paste(img, mask=img.split()[-1] if img.mode == 'RGBA' else None)
                    img = background
                
                # Dimensiones objetivo: 1200x630px (ideal para blogs y redes sociales)
                target_width = 1200
                target_height = 630
                
                # Calcular el ratio y recortar desde el centro
                img_ratio = img.width / img.height
                target_ratio = target_width / target_height
                
                if img_ratio > target_ratio:
                    # Imagen muy ancha, recortar los lados
                    new_width = int(img.height * target_ratio)
                    offset = (img.width - new_width) // 2
                    img = img.crop((offset, 0, offset + new_width, img.height))
                else:
                    # Imagen muy alta, recortar arriba/abajo
                    new_height = int(img.width / target_ratio)
                    offset = (img.height - new_height) // 2
                    img = img.crop((0, offset, img.width, offset + new_height))
                
                # Redimensionar a tamaño final
                img = img.resize((target_width, target_height), Image.Resampling.LANCZOS)
                
                # Guardar imagen procesada
                output = BytesIO()
                img.save(output, format='JPEG', quality=90, optimize=True)
                output.seek(0)
                
                # Reemplazar el archivo original
                self.imagen = InMemoryUploadedFile(
                    output,
                    'ImageField',
                    f"{self.imagen.name.split('.')[0]}.jpg",
                    'image/jpeg',
                    sys.getsizeof(output),
                    None
                )
            except Exception as e:
                # Si hay error al procesar, continuar con la imagen original
                print(f"Error al procesar imagen: {e}")
        
        super().save(*args, **kwargs)

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
