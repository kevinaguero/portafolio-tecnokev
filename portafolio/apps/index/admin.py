from django.contrib import admin
from .models import AboutSection, AboutBadge, AboutListItem

# Register your models here.

class AboutBadgeInline(admin.TabularInline):
    model = AboutBadge
    extra = 1
    fields = ['nombre', 'icono', 'icono_tipo', 'orden']

class AboutListItemInline(admin.TabularInline):
    model = AboutListItem
    extra = 1
    fields = ['texto', 'orden']

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'tipo', 'orden', 'vigencia']
    list_filter = ['tipo', 'vigencia']
    search_fields = ['titulo', 'descripcion']
    ordering = ['orden']
    
    fieldsets = (
        ('Información Básica', {
            'fields': ('tipo', 'titulo', 'descripcion', 'orden', 'vigencia')
        }),
        ('Diseño', {
            'fields': ('icono',),
            'description': 'Clase de icono Font Awesome (ej: fa-solid fa-briefcase)'
        }),
        ('Card Principal (solo para tipo Principal)', {
            'fields': ('avatar', 'usuario'),
            'classes': ('collapse',),
            'description': 'Estos campos solo aplican a la card principal'
        }),
    )
    
    def get_inlines(self, request, obj=None):
        """Mostrar inlines según el tipo de card"""
        if obj:
            if obj.tipo == 'principal':
                return [AboutBadgeInline]
            elif obj.tipo == 'secundaria':
                return [AboutListItemInline]
        return []
    
    def get_readonly_fields(self, request, obj=None):
        """Hacer campos readonly según el tipo"""
        if obj and obj.tipo == 'secundaria':
            return ['avatar', 'usuario']
        return []
