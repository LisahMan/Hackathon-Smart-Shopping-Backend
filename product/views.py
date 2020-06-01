from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Product
from .serializers import ProductSerializer

class ProductDetail(APIView):

	def get(self,request,bar_id):
		try:
			product = Product.objects.get(barcode = bar_id)
			serializers = ProductSerializer(product)
			return Response(serializers.data)
		except Product.DoesNotExist:
			raise Http404

class OrderProduct(APIView):

	def get(self,request,rf_id):
		try:
			product = Product.objects.get(rfid = rf_id)
			serializers = ProductSerializer(product)
			return Response(serializers.data)
		except product.DoesNotExist:
			raise Http404

class SearchProduct(APIView):

	def post(self,request):
		name = request.data['name']
		try:
			searched_product = Product.objects.filter(name__icontains = name)
			serializers = ProductSerializer(searched_product,many = True)
			return Response(serializers.data)
		except Product.DoesNotExist:
			raise Http404