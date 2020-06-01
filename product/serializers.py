from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

	class Meta:
		model = Product
		fields = ('rfid','barcode','name','image','price','manufactured_date','expiry_date','description','section')

