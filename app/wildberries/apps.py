from django.apps import AppConfig


class WildberriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wildberries'
    def ready(self):
        from .scheduler import start_scheduler  # Import here to avoid circular dependencies
        start_scheduler()