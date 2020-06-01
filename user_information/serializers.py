from rest_framework import serializers
from django.contrib.auth.models import User 
from .models import UserInformation

class UserSerializer(serializers.ModelSerializer):

	phone_number = serializers.IntegerField(source = 'user_information.phone_number',write_only=True)
	id = serializers.CharField(read_only = True)

	class Meta:
		model = User 
		fields = ('id','username','password','phone_number')
		extra_kwargs = {'password' : {'write_only' : True}}


	def create(self,validated_data):

		user = User.objects.create_user(username = validated_data['username'],password = validated_data['password'])
		UserInformation.objects.create(user = user,phone_number = validated_data['user_information']['phone_number'])
		return user