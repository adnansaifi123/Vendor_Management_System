from django.conf.urls import include
from django.urls import path
from . views import PurchaseOrder,PurchaseOrderDetails,PurchaseOrderAcknowledge

urlpatterns=[
    path('api/purchase_orders', PurchaseOrder.as_view(), name='get_post_PO'),
    path('api/purchase_orders/<str:po_id>', PurchaseOrderDetails.as_view(), name='get_delete_update_PO'),
    path('api/purchase_orders/<str:po_id>/acknowledge',PurchaseOrderAcknowledge.as_view())
]