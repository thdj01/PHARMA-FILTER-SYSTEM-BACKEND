# cleaning/apps.py

from django.apps import AppConfig

class CleaningConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cleaning'

    def ready(self):
        # This imports the signals file when the app is ready,
        # connecting the receivers.
        import cleaning.signals