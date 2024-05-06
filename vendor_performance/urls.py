from django.conf.urls import include
from django.urls import path
from .views import vendor_performance

urlpatterns=[
    path('api/vendors/<str:vendor_id>/performance',vendor_performance.as_view(),name='vendor_performance'),
]