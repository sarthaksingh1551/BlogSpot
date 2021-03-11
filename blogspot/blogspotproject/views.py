from django.shortcuts import render, HttpResponse, redirect
from datetime import datetime
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages

def homepage(request):
    return render(request, "homepage.html")

def about(request):
    return render(request, "about.html")
