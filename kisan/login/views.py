from django.http import HttpResponse
from django.shortcuts import render

def index2(request):
	return render(request,'login/login.html')


def details2(request):
	return render(request,'login/logout.html')


	

