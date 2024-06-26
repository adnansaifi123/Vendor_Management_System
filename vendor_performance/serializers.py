from rest_framework import serializers
from .models import HistoricalPerformance

class vendorPerformanceSerailizer(serializers.ModelSerializer):

    class Meta:
        model=HistoricalPerformance
        fields=['vendor','date','on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']