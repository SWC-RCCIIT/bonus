from . import views
from django.urls import path
from register.models import Farmer, Buyer

urlpatterns = [
    path('detailf/',views.detailf,name="detailf"),
    path('',views.index,name="index"),
    
]
