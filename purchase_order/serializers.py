from rest_framework import serializers
from .models import purchase_orders

class PurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=purchase_orders
        fields=['po_number','vendor','order_date','delivery_date','items',
                'quantity','status','quality_rating','issue_date','acknowledgment_date']
        read_only_field=['po_number']

class PurchaseOrderSerializerPost(serializers.ModelSerializer):
    class Meta:
        model=purchase_orders
        fields=['po_number','vendor','order_date','delivery_date','items',
                'quantity','status','quality_rating','issue_date','acknowledgment_date']