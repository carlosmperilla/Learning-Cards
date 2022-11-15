from django.apps import AppConfig


class CardConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'card'
    verbose_name: str = "Gestión de tarjetas"
