from .models import vendors
from rest_framework import serializers

class vendorsSerializer(serializers.ModelSerializer):
    class Meta:
        model=vendors
        fields=['name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']
        read_only_fields=['vendor_code']

class vendorsSerializerPost(serializers.ModelSerializer):
    class Meta:
        model=vendors
        fields=['name','contact_details','address','vendor_code','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']