from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',include('register.urls'),name="register"),
    path('',include('home.urls')),
    path('contact/',include('contact.urls')),
    path('buysell/',include('buysell.urls')),
    path('login/',include('login.urls')),
    
]
