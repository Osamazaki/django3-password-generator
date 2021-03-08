from django.shortcuts import render
import random
# Create your views here.
from django.http import HttpResponse


def home(request):
    return render(request, "home.html")


def password(request):
    thepass = ""
    chars = list("abcdefghijklnopqrstuvwsyz")
    if request.GET.get('uppercase'): #GG
        chars.extend("ABCDEFGHIJKLMNOPQRSTUVWSYZ")
    if request.GET.get('numbers'):
        chars.extend("1234567890")
    if request.GET.get('special characters'):
        chars.extend("!@#$%^&*()")
    for x in range(11):
        thepass += random.choice(chars)
    return render(request, "password.html", {"password": thepass})


def about(request):
    return render(request, "about.html")