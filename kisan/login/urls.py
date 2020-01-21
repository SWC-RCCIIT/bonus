from . import views
from django.urls import path


urlpatterns = [
    path('login/',views.index2,name="index2"),
    path('logout/',views.details2,name="details2")
    
    
]
