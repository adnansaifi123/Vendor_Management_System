from django.utils import timezone
from .models import purchase_orders
from .serializers import PurchaseOrderSerializer, PurchaseOrderSerializerPost
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

# Create your views here.

class PurchaseOrder(APIView):
    def get_queryset(self,request):
        orders=purchase_orders.objects.all()
        return orders


    def get(self,request):
        orders=self.get_queryset(request)
        # print(orders)
        if not orders:
            content = {
                        'status': 'No Purchase order Found!!'
                    }
            return Response(content,status=status.HTTP_204_NO_CONTENT)

        serializer=PurchaseOrderSerializer(orders,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        # Create Purchase Order
        serializer=PurchaseOrderSerializerPost(data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            # update_metrics(serializer.instance)
            return Response({'status':f"Purchase Order {serializer.data['po_number']} Created Successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


class PurchaseOrderDetails(APIView):

    def get(self,request,po_id):
        try:
            order_detail=purchase_orders.objects.get(po_number=po_id)
        except purchase_orders.DoesNotExist:
            content={
                'status': 'Not Found'
            }
            return Response(content,status=status.HTTP_204_NO_CONTENT)
        serializer = PurchaseOrderSerializer(order_detail)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self,request,po_id):
        order= purchase_orders.objects.get(po_number=po_id)
        print(order)
        serializer=PurchaseOrderSerializer(order,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            # update_metrics.send(serializer.instance)
            # update_metrics(serializer.instance)
            return Response(f"Order {po_id} Updated Successfully",status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,po_id):
        try:
            order=purchase_orders.objects.get(po_number=po_id)
        except purchase_orders.DoesNotExist:
            content={
                "status":f"Purchase Order-{po_id} not found!!"
            }
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        order.delete()
        return Response(f"Purchase Order {po_id} Deleted Successfully", status=status.HTTP_200_OK)


class PurchaseOrderAcknowledge(APIView):
    def post(self, request, po_id):
        try:
            order_details = purchase_orders.objects.get(po_number=po_id)
        except purchase_orders.DoesNotExist:
            return Response({'status': 'Purchase Order not found'}, status=status.HTTP_404_NOT_FOUND)

        order_details.acknowledgment_date = timezone.now()
        serializer = PurchaseOrderSerializer(order_details)
        print(serializer.data)

        try:
            order_details.save()
            return Response({'status': 'Purchase Order acknowledged successfully',
                             'data': f'{serializer.data}'}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'status': 'Failed to acknowledge Purchase Order',
                             'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)