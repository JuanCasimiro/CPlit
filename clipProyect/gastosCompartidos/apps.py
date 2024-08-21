from django.apps import AppConfig


class GastoscompartidosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'gastosCompartidos'

    def ready(self):
        import gastosCompartidos.signals