from django.db import models

class Product(models.Model):

	rfid = models.CharField(max_length=20)
	barcode = models.CharField(max_length=20)
	name = models.CharField(max_length=50)
	image = models.ImageField(upload_to = 'media',max_length=255,null=True)
	price = models.IntegerField(default=0)
	manufactured_date = models.DateField()
	expiry_date = models.DateField()
	description = models.TextField()
	section = models.CharField(max_length=5)

	def __str__(self):
		return self.name + " " + str(self.price)
