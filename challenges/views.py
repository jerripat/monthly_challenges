"""
Module docstring describing the purpose of the module.
"""

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse


monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": None,
}


def index(request):

    months = list(monthly_challenges.keys())
    return render(request, "challenges/index.html", {"months": months})


def monthly_challenge(request, month):
    """
    View function to display the monthly challenge for a given month.
    """
    try:
        challenge_text = monthly_challenges[month]
        month_name = month
        return render(
            request,
            "challenges/challenge.html",
            {"text": challenge_text, "month_name": month_name},
        )
    except KeyError:
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")


def monthly_challenge_by_number(request, month):
    """
    View function to display the monthly challenge for a given month number.
    """
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound("<h1>This month is not supported!</h1>")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
