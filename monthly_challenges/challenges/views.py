from django.urls import path
from django.http import HttpResponse,HttpResponceNotFound

def monthly_challenge(request, month):
    return HttpResponse(month)
