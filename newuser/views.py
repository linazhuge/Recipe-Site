from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import NewUserForm
from django.contrib import messages

# Create your views here.
def register_view(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("select")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="register.html", context={"form":form})