from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1> This page will save our contact details</h1>")
