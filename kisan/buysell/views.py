from django.http import HttpResponse
from django.shortcuts import render
from register.models import Farmer

def index(request):
	return HttpResponse("<h1>Products will be listed here</h1>")

def detailf(request):
	all_farmers=Farmer.objects.all()
	print(Farmer.objects.all())
	return render(request,'buysell/f.html', {'farmers' : all_farmers})

	

	

