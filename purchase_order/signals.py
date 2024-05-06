from datetime import datetime, timedelta
from django.db.models import ExpressionWrapper, Avg, DurationField, F
from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from .models import purchase_orders
from vendor_performance.models import HistoricalPerformance



@receiver([post_save,post_delete],sender=purchase_orders)
def update_metrics(sender, instance, **kwargs):
    print('Inside metrics calculation...')
    vendor=instance.vendor

    completed_orders = purchase_orders.objects.filter(vendor=vendor, status='completed')
    total_completed_orders = completed_orders.count()
    if total_completed_orders == 0:
        vendor.on_time_delivery_rate = 0
        vendor.quality_rating_avg = 0
        vendor.average_response_time = 0
        vendor.fulfillment_rate = 0

    else:
        # Update on_time_delivery_rate
        total_completed_PO=purchase_orders.objects.filter(vendor=vendor,status='completed').count()
        on_time_completd_PO=purchase_orders.objects.filter(vendor=vendor,status='completed',
                                                           delivery_date__lte=F('acknowledgment_date')).count()

        on_time_delivery_rate=(on_time_completd_PO/total_completed_PO)*100 if total_completed_PO>0 else 0

        #update_quality_rating
        completed_po=purchase_orders.objects.filter(vendor=vendor,status='completed').exclude(quality_rating__isnull=False)
        average_quality_rating=completed_po.aggregate(avg_rating=Avg('quality_rating'))['avg_rating'] or 0

        # Average Response Time:
        response_times = purchase_orders.objects.filter(vendor=vendor, acknowledgment_date__isnull=False).annotate(
            response_time=ExpressionWrapper(F('acknowledgment_date') - F('issue_date'), output_field=DurationField())
        )
        avg_response_time = response_times.aggregate(avg_time=Avg('response_time'))['avg_time'] or timedelta(0)
        avg_response_time_seconds = avg_response_time.total_seconds() if avg_response_time is not None else 0

        #Fulfillment
        total_issued_po=purchase_orders.objects.filter(vendor=vendor).count()
        successful_po=purchase_orders.objects.filter(vendor=vendor,status='completed').count()
        fulfillment_rate=(successful_po/total_issued_po)*100 if total_issued_po > 0 else 0

        vendor.on_time_delivery_rate = on_time_delivery_rate
        vendor.quality_rating_avg = average_quality_rating
        vendor.average_response_time = avg_response_time_seconds
        vendor.fulfillment_rate = fulfillment_rate
        print(vendor.average_response_time)

    vendor.save()
    print('vendor metrics updated')
    HistoricalPerformance.objects.create(
        vendor=vendor,
        on_time_delivery_rate=vendor.on_time_delivery_rate,
        quality_rating_avg=vendor.quality_rating_avg,
        average_response_time=vendor.average_response_time,
        fulfillment_rate=vendor.fulfillment_rate
    )
