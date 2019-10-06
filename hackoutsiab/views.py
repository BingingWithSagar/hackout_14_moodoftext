from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login

# Create your views here.


def signup(request):
	if request.method == "POST":
		form = UserCreationForm(request.POST)
		if form.is_valid():
			form.save()
			return HttpResponse("<h1>register works</h1>")


	form = UserCreationForm()
	return render(request,'hackoutsiab/signup.html',{'form':form})

def login_view(request):
	if request.method == "POST":

		form = AuthenticationForm(data = request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request,user)
			user=request.user.username
			if user == "psych":
				return redirect('/psych')			

		return redirect('/entry')
	else:
		form = AuthenticationForm()
		return render(request,'hackoutsiab/login.html',{'form':form})




