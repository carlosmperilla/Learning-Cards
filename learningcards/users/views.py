from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages


# Create your views here.
def singup_user(request):
    """
        Validate and register the user.
    """

    return HttpResponse("SignUp")

def login_user(request):
    """
        Validate and loggin the user.
    """

    return HttpResponse("LogIn")

@login_required
def logout_user(request):
    """
        Logout user session.
    """

    return HttpResponse("LogOut")