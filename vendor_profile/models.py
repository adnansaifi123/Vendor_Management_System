from django.db import models
# Create your models here.

class vendors(models.Model):
    name=models.CharField(max_length=50)
    contact_details=models.TextField()
    address=models.TextField()
    vendor_code=models.CharField(unique=True,max_length=10,blank=False)
    on_time_delivery_rate=models.FloatField(default=0.0)
    quality_rating_avg=models.FloatField(default=0.0)
    average_response_time=models.FloatField(default=0.0)
    fulfillment_rate=models.FloatField(default=0.0)
