from django import forms 
from models import BMR

class BMRform(forms.ModelForm):
	class Meta:
		model = BMR
		fields = {'user', 'weight', 'height', 'sex', 'age'}