from django.urls import path
from . import views

urlpatterns = [
    path('httpview', views.firstview, name="httpview"),
    path('abc', views.secondview, name="testingview"),
    path('custom', views.customwebpage, name="Webpage"),
]