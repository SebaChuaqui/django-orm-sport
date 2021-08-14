from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name="index"),
	path('initialize', views.make_data, name="make_data"),
	path('index2', views.index2, name="index2")
]
