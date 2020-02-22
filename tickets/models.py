from django.db import models

from django.contrib.auth.models import User
# Create your models here.
class Banks(models.Model):
	# ifsc code for bank
	ifsc = models.CharField(max_length=100)
	# bank_id
	bank_id = models.IntegerField()
	# branch
	branch = models.CharField(max_length=100)
	# address
	address = models.CharField(max_length=255)
	# City where bank is present
	city = models.CharField(max_length=100)
	# District of the bank
	district = models.CharField(max_length=100)
	# State where bank is present
	state = models.CharField(max_length=100)
	# Name of the bank
	bank_name = models.CharField(max_length=100)
	

	def __str__(self):
		return "{} - {}".format(self.bank_name, self.city)



