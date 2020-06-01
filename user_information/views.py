from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from .serializers import UserSerializer

class UserCreate(APIView):

	def post(self,request):
		serializers = UserSerializer(data = request.data)
		if serializers.is_valid():
			serializers.save()
			return Response(serializers.data,status = status.HTTP_201_CREATED)
		return Response(serializers.errors,status = status.HTTP_400_BAD_REQUEST)

class UserDelete(APIView):

	def delete(self,request,pk):
		try:
			user = User.objects.get(pk=pk)
		except User.DoesNotExist:
			raise Http404

		user.delete()
		return Response(status = status.HTTP_204_NO_CONTENT)


class CheckUserDetail(APIView):

	def post(self,request):

		username = request.data['username']
		password = request.data['password']

		try:
			user = authenticate(username=username,password = password)
			if user:
				serializers = UserSerializer(user)
				return Response(serializers.data,status = status.HTTP_202_ACCEPTED)
			return Response(data = 'error',status = status.HTTP_400_BAD_REQUEST)
		except User.DoesNotExist:
			raise Http404