from django.contrib import admin
from .models import Blog, Comentario

# Register your models here.

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'autor', 'fecha', 'vigencia']
    list_filter = ['vigencia', 'fecha', 'categorias']
    search_fields = ['titulo', 'descripcion', 'contenido']
    prepopulated_fields = {'slug': ('titulo',)}
    date_hierarchy = 'fecha'
    ordering = ['-fecha']
    filter_horizontal = ['categorias', 'colaboradores']
    
    fieldsets = (
        ('Información Principal', {
            'fields': ('titulo', 'slug', 'descripcion', 'autor')
        }),
        ('Contenido', {
            'fields': ('contenido',)
        }),
        ('Imagen Destacada', {
            'fields': ('imagen', 'imagen_epigrafe'),
            'description': 'La imagen se recortará automáticamente a 1200x630px'
        }),
        ('Colaboradores', {
            'fields': ('colaboradores',),
            'description': 'Selecciona los usuarios que colaboraron en este artículo'
        }),
        ('Categorización', {
            'fields': ('categorias', 'vigencia')
        }),
    )

@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ['autor', 'blog', 'fecha', 'aprobado']
    list_filter = ['aprobado', 'fecha']
    search_fields = ['autor', 'email', 'contenido']
    actions = ['aprobar_comentarios']
    
    def aprobar_comentarios(self, request, queryset):
        queryset.update(aprobado=True)
    aprobar_comentarios.short_description = "Aprobar comentarios seleccionados"
