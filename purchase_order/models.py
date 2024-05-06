from django.db import models
# from vendor_profile.models import vendors
# Create your models here.

class purchase_orders(models.Model):
    po_number=models.CharField(max_length=20,unique=True)
    vendor=models.ForeignKey('vendor_profile.vendors',on_delete=models.CASCADE, to_field='vendor_code')
    order_date=models.DateTimeField()
    delivery_date=models.DateTimeField()
    items=models.JSONField()
    quantity=models.IntegerField()
    status=models.CharField(max_length=25)
    quality_rating=models.FloatField(null=True,blank=True)
    issue_date=models.DateTimeField(auto_now_add=True)
    acknowledgment_date=models.DateTimeField(null=True,blank=True)

    # def save(self):
    #     super.save()
    #     if self.status=='completed':
    #         self.vendors.update_quality_rating()
    #     if self.quality_rating is not None:
    #         self.vendors.update_quality_rating_avg()
    #     if self.acknowledgment_date is not None:
    #         self.vendors.update_average_response_time()
    #     self.vendors.update_fulfillment_rate()