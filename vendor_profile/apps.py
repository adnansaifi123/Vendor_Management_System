from django.apps import AppConfig


class VendorProfileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'vendor_profile'

    def ready(self):
        import purchase_order.signals

