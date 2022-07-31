from django.apps import AppConfig


class PaymentAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'payment_app'

    def ready(self):
        import payment_app.signals
