from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from forms import LoginForm, SignupForm

# Create your views here.

def index(request):

	return render(request, "index.html")

def login_page(request):

	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
				return HttpResponseRedirect('/main/%s'%user.username)
	form = LoginForm()
	return render(request, "login.html", {'form': form})

def main_page(request, username):

	user = get_object_or_404(User, username=username)
	return render(request, "main.html", {'username': user.username})

def signup_page(request):

	if request.method=='POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			user = User.objects.create_user(
				username = 	form.cleaned_data['username'],
				password = form.cleaned_data['password1'],
				email = form.cleaned_data['email']
				)
			return HttpResponseRedirect('/signup/success/')
	form = SignupForm()
	return render(request, "register.html", {'form': form})

@login_required(login_url='/login/')
def logout_page(request):
	logout(request)
	return HttpResponseRedirect('/')

		