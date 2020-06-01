from django.db import models
from django.contrib.auth.models import User 

class Bill(models.Model):

	user = models.ForeignKey(User,related_name='user_id')
	total = models.IntegerField()

	def __str__(self):
		return str(self.user)+str(self.total)



class Order(models.Model):

	bill = models.ForeignKey(Bill,related_name='orders',on_delete=models.CASCADE)
	name = models.CharField(max_length=50)
	price = models.IntegerField(default=0)

	def __str__(self):
		return str(self.bill) + " " + self.name + " " + str(self.price)

