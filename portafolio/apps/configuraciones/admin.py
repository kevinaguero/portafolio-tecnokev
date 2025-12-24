from django.contrib import admin
from .models import Categoria, Carousel

# Register your models here.

@admin.register(Carousel)
class CarouselAdmin(admin.ModelAdmin):
    list_display = ('orden', 'titulo', 'vigencia', 'nombre_boton', 'fecha_creacion')
    list_display_links = ('titulo',)
    list_editable = ('orden', 'vigencia')
    list_filter = ('vigencia', 'fecha_creacion')
    search_fields = ('titulo', 'descripcion')
    filter_horizontal = ('categorias',)
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo', 'descripcion', 'imagen')
        }),
        ('Categorías', {
            'fields': ('categorias',),
            'description': 'Selecciona las categorías relacionadas (opcional)'
        }),
        ('Botón de Acción', {
            'fields': ('nombre_boton', 'link_boton'),
            'description': 'Si no quieres mostrar un botón, deja estos campos vacíos'
        }),
        ('Configuración', {
            'fields': ('orden', 'vigencia')
        }),
    )

admin.site.register(Categoria)