from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Bill
from .models import Order
from .serializers import BillSerializer
from .serializers import OrderSerializer

class BillDetail(APIView):

	def get(self,request,pk):
		try:
			bill = Bill.objects.get(pk=pk)
		except Bill.DoesNotExist:
			raise Http404

		serializers = BillSerializer(bill)
		return Response(serializers.data)

class BillCreate(APIView):

	def post(self,request):
		serializers = BillSerializer(data = request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data,status = status.HTTP_201_CREATED)
		return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)

class OrderCreate(APIView):

	def post(self,request):
		serializers = OrderSerializer(data = request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data,status = status.HTTP_201_CREATED)
		return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)