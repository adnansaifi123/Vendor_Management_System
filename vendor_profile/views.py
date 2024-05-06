from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import vendorsSerializer, vendorsSerializerPost
from .models import vendors
# Create your views here.

class vendorsList(APIView):

    def get_queryset(self,request):
        try:
            vendor_details=vendors.objects.all()
            # print(vendor_details)
        except vendors.DoesNotExist:
            content={
                'status':"No Vendors found!!"
            }
            return content
        return vendor_details


    def get(self,request):
        vendors_data=self.get_queryset(request)
        serializer= vendorsSerializer(vendors_data,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer=vendorsSerializerPost(data=request.data)
        if serializer.is_valid():
            vendor=serializer.save()
            return Response(f"New Vendor {vendor.name}, vendor_id: {vendor.vendor_code} is created successfully ",
                            status=status.HTTP_201_CREATED)
            # return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class vendorDetail(APIView):

    def get(self,request,vendor_id):
        try:
            data=vendors.objects.get(vendor_code=vendor_id)
        except vendors.DoesNotExist:
            content = {
                'status': "No Vendors found!!"
            }
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        serializer=vendorsSerializer(data)
        return Response(serializer.data,status=status.HTTP_200_OK)

    def put(self, request,vendor_id):
        try:
            vendor=vendors.objects.get(vendor_code=vendor_id)
            # print(data)
        except vendors.DoesNotExist :
            content = {
                'status': "No Vendors found!!"
            }
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        serializer=vendorsSerializer(vendor,data=request.data)
        # print(serializer)
        if serializer.is_valid():
            # print(serializer.validated_data)
            serializer.save()
            # return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(f"Vendor {vendor.name}, vendor_id: {vendor.vendor_code} is Updated successfully ",
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,vendor_id):
        try:
            vendor=vendors.objects.get(vendor_code=vendor_id)
        except vendors.DoesNotExist :
            content = {
                'status': "No Vendors found!!"
            }
            return Response(content,status=status.HTTP_400_BAD_REQUEST)
        vendor.delete()
        return Response(f"Vendor {vendor.vendor_code} Deleted Successfully",status=status.HTTP_200_OK)






