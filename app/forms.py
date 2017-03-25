from django import forms
import re
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

class LoginForm(forms.Form):
	
	username = forms.CharField(
								max_length=30, 
								widget = forms.TextInput(attrs={'placeholder': 'Username', 'name': 'fname'})
							)
	password = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'name': 'pword'})
		)

class SignupForm(forms.Form):

	username = forms.CharField(
								label='username', 
								max_length=30, 
								widget = forms.TextInput(attrs={'placeholder': 'Username', 'name': 'fname'})
							)

	email = forms.EmailField(label='email', widget = forms.TextInput(attrs={'placeholder': 'Email', 'name': 'email'}))
	
	password1 = forms.CharField(
		label='password1', 
		widget=forms.PasswordInput(attrs={'placeholder': 'Password', 'name': 'pword'})
		)

	password2 = forms.CharField(
		label='password2',
		widget=forms.PasswordInput(attrs={'placeholder': 'Password Again', 'name': 'pword2'})
		)


	def clean_password2(self):
		if 'password1' in self.cleaned_data:		
		#forms.clean_data is used to access the validated form input
			password1 = self.cleaned_data['password1']
			password2 = self.cleaned_data['password2']
			if password1 == password2:
				return password2
			raise forms.ValidationError('Passwords do not match!')

	def clean_username(self):
		username = self.cleaned_data['username']
		if not re.search(r'^\w+$', username):
		# the above line checks if the passed string is
		# comprised of alphanumeric characters and underscore only
		# and if not then it raises a validation error. 
			raise forms.ValidationError('Username can contain alphanumeric charcater snd underscores only.')

		try:
			User.objects.get(username=username)
		except ObjectDoesNotExist:
			return username
		raise forms.ValidationError('Username is already taken.')