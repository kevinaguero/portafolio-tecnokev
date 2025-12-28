from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Categoria, Carousel, Profile

# Register your models here.

# Inline para el perfil del usuario
class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Perfil'
    fields = ('avatar', 'bio', 'website', 'github', 'linkedin', 'twitter')

# Extender el admin de User para incluir el perfil
class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'get_avatar')
    
    def get_avatar(self, obj):
        if hasattr(obj, 'profile') and obj.profile.avatar:
            return f'✓ Avatar'
        return '✗ Sin avatar'
    get_avatar.short_description = 'Foto de Perfil'

# Re-registrar UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

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