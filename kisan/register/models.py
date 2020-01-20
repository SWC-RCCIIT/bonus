from django.db import models

class detail(models.Model):
	
	First_name = models.CharField(max_length=100)
	Last_name=models.CharField(max_length=100)
	Users_choices= (('Farmer','Farmer'),('Buyer','Buyer'))
	Users_type=models.CharField(max_length=10,choices=Users_choices,default='Farmer')	
	Phone_number=models.CharField(max_length=10)
	Address=models.CharField(max_length=250)
	field_area=models.IntegerField()



