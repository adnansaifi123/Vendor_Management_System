from django.contrib import admin
from django.urls import path
from .views import vendorsList,vendorDetail

urlpatterns = [
    path('api/vendors', vendorsList.as_view(),name='get_post_vendor_List'),
    path('api/vendors/<str:vendor_id>', vendorDetail.as_view(),name='get_post_vendor_details'),
]
