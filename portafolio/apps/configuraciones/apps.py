from django.apps import AppConfig


class ConfiguracionesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.configuraciones'
    
    def ready(self):
        import apps.configuraciones.models  # Importar signals
