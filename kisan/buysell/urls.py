from . import views
from django.urls import path
from register.models import Farmer, Buyer

urlpatterns = [
    path('',views.index,name="index"),
    path('detailf/',views.detailf,name="detailf"),
    
]
