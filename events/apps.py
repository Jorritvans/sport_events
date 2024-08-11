from django.apps import AppConfig

# Configuration class for the events application


class EventsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    # Default field type for auto-incrementing primary keys
    name = 'events'  # Name of the application
