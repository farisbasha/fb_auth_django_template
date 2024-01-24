from django.apps import AppConfig


class DrfRegistrationConfig(AppConfig):
    """
    The app config

    Args:
        AppConfig (class): Class representing a Django application and its configuration
    """
    name = 'apps.drf_registration'
    
    def ready(self):
        import apps.drf_registration.signals
