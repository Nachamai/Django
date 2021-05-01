from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def firstview(request):
    return HttpResponse("Hi this is running on your django server")

def secondview(request):
    return HttpResponse("Working fine")

def customwebpage(request):
    context = {"tag_var":"tag_var"}
    return render(request,"first.html",context)