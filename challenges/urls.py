"""
Module docstring describing the purpose of the module.
"""

from django.urls import path
from challenges import views


urlpatterns = [
    
    path("", views.index),
    path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.monthly_challenge, name="month-challenge"),
]
