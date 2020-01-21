from django.http import HttpResponse


def index(request):
	return HttpResponse("<h1>This will be the main registration page</h1>")

	