from django.db import models
from django.contrib.auth.models import User

class BMR(models.Model):

	GENDER_CHOICES = (
   ('M', 'Male'),
   ('F', 'Female')
)

	user = models.ForeignKey(User)
	weight= models.FloatField(null=True, blank=True, default=None)
	height = models.FloatField(null=True, blank=True, default=None)
	sex = models.CharField(choices=GENDER_CHOICES, max_length=128)
	age = models.IntegerField(default=0)
	BMR = models.FloatField(default=0, null=True)

class Disease(models.Model):
	disease = models.CharField(max_length=500)

class Diet(models.Model):

	Diet_choice = (
		('V','Veg'),
		('NV','Non Veg'),
		('M','mixed')
		)
	diet = models.CharField(choices=Diet_choice, max_length=128)



