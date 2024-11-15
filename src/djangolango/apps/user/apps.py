from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangolango.apps.user'

    def ready(self):
        from . import views