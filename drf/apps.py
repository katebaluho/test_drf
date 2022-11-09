from django.apps import AppConfig


class DrfConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'drf'

    def ready(self):
        from . import signals
        super().ready()