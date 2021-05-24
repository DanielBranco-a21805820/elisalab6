from django.shortcuts import render
from django.urls import path
from . import views
app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('guito', views.guito_page_view, name="guito"),
    path('fotos', views.fotos_page_view, name="fotos")
]