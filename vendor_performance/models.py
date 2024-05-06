from django.db import models
# Create your models here.


class HistoricalPerformance(models.Model):
    vendor = models.ForeignKey('vendor_profile.vendors', on_delete=models.CASCADE, to_field='vendor_code')
    date = models.DateTimeField(auto_now=True)
    on_time_delivery_rate = models.FloatField()
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField(default=0.0)
    fulfillment_rate = models.FloatField()
