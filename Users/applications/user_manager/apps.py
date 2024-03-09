from django.apps import AppConfig

# Se registra la aplicacion para el Gestor de Usuario
class UserManagerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'applications.user_manager'