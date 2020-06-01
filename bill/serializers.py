from rest_framework import serializers
from .models import Bill
from .models import Order

class OrderSerializer(serializers.ModelSerializer):


	class Meta:
		model = Order
		fields = ('bill','name','price')
		extra_kwargs = {'bill' : {'read_only' : True}}

class BillSerializer(serializers.ModelSerializer):

	orders = OrderSerializer(many = True)
	id = serializers.CharField(read_only = True)

	class Meta:
		model = Bill
		fields = ('id','user','total','orders')

	def create(self,validated_data):
		bill = Bill.objects.create(user = validated_data['user'],total = validated_data['total'])
		for order in validated_data['orders']:
			Order.objects.create(bill = bill,name = order['name'],price = order['price'])
		return bill

