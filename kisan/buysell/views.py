from django.http import HttpResponse

def index(request):
	return HttpResponse("<h1>Products will be listed here</h1>")

	

