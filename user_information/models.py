from django.db import models
from django.contrib.auth.models import User 

class UserInformation(models.Model):

	user = models.OneToOneField(User,related_name='user_information',on_delete=models.CASCADE)
	phone_number = models.IntegerField(default=0)

	def __str__(self):
		return str(self.user) + " " + str(self.phone_number)
