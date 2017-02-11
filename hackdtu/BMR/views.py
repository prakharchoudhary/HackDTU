from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import forms	

@login_required(login_url='/login/')
def details(request):
	user = User.objects.get(username=request.user.username)
	if request.method == "POST":
		form = forms.BMRform(request.POST)
		if form.is_valid():
			if(form.cleaned_data['sex']=='M'):
				b = 66.5 + ( 13.75 * form.cleaned_data['weight']) + ( 5.003 * form.cleaned_data['height']) - ( 6.755 * form.cleaned_data['age'])
			else:
				b = 655.1 + ( 9.563 * form.cleaned_data['weight']) + ( 1.850 * form.cleaned_data['height'] ) - ( 4.676 * form.cleaned_data['age'] )
			bmr = BMR.objects.get_or_create(
				user = user,
				weight = form.cleaned_data['weight'],
				heigth = form.cleaned_data['height'],
				sex = form.cleaned_data['sex'],
				age = form.cleaned_data['age'],
				BMR = b,
				)
			return HttpResponseRedirect('/%s/main/'%user.username)

	form = forms.BMRform()
	return render(request, "BMRcalc.html", {'form': form})
