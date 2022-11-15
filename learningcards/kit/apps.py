from django.apps import AppConfig


class KitConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'kit'
    verbose_name: str = "Gestión de kits"
