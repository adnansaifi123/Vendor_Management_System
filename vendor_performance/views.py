from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import HistoricalPerformance
from .serializers import vendorPerformanceSerailizer
# Create your views here.

class vendor_performance(APIView):

    def get(self, request, vendor_id):
        vendorPerformance = HistoricalPerformance.objects.filter(vendor=vendor_id)
        print(vendorPerformance)
        # to be checked
        if vendorPerformance is None:
            return Response("No Data found", status=status.HTTP_204_NO_CONTENT)
        serializer = vendorPerformanceSerailizer(vendorPerformance, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
