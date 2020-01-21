from django.db import models

class Farmer(models.Model):
	
	First_name = models.CharField(max_length=100,default='None')
	Last_name=models.CharField(max_length=100,default='None')	
	Phone_number=models.CharField(max_length=10,primary_key=True,default='None')
	Address=models.CharField(max_length=250,default = 'None')
	Product=models.CharField(max_length=100,default='None')
	Price=models.IntegerField(default=0)

	

class Buyer(models.Model):
	
	first_name = models.CharField(max_length=100,default='None')
	last_name=models.CharField(max_length=100,default='None')	
	phone_number=models.CharField(max_length=10,default='None')
	address=models.CharField(max_length=250,default='None')
		



