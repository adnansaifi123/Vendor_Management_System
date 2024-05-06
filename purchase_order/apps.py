from django.apps import AppConfig

class PurchaseOrderConfig(AppConfig):
    name = 'purchase_order'

    def ready(self):
        import purchase_order.signals
