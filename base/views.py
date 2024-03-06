from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial
from django.contrib.auth.forms import UserCreationForm
# Create your views here.

def Homepage(request):
	return render(request,
				"base/home.html",
				{"tutorials":Tutorial.objects.all})

def Register(request):
	form = UserCreationForm

	return render(request,
				  "base/register.html",
				  {"form":form})