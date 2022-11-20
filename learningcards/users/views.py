from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import LoginForm, SignUpForm
# from django.utils.translation import gettext
from django.utils import translation

# Create your views here.
def singup_user(request):
    """
        Validate and register the user.
    """

    if request.user.is_authenticated:
        return redirect('index')
    
    if request.method == 'POST':
        if request.POST.get('lc-lang') != 'es':
            translation.activate('en')
            success_message_text = """
                You have 
                <span class="popup__span">&nbsp;successfully</span>
                <span class="popup__span">&nbsp;sign up!</span>
            """
        else:
             translation.activate('es')
             success_message_text = """
                Te has 
                <span class="popup__span">&nbsp;registrado</span>
                <span class="popup__span">&nbsp;correctamente!</span>
            """

        data = {}
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            user = signup_form.save()
            messages.success(request, success_message_text)
            login(request, user)

            data['redirect_url'] = reverse('index')
            return JsonResponse(data)
        
        data['errors'] = signup_form.errors.as_ul()
        return JsonResponse(data)

    return redirect('index')


def login_user(request):
    """
        Validate and loggin the user.
    """
    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        data = {}
        login_form = LoginForm(data=request.POST)

        if login_form.is_valid():
            user = login_form.get_user()
            if user:
                if request.POST.get('lc-lang') == 'es':
                    success_message_text = """
                        Has
                        <span class="popup__span">&nbsp;iniciado&nbsp;</span>
                        sesión
                        <span class="popup__span">&nbsp;correctamente!</span>
                    """
                else:
                    success_message_text = """
                        You
                        <span class="popup__span">&nbsp;have&nbsp;</span>
                        successfully
                        <span class="popup__span">&nbsp;logged</span>
                        in!
                    """
                login(request, user)
                messages.success(request, success_message_text)
                data['redirect_url'] = reverse('index')
                return JsonResponse(data)
        
        if request.POST.get('lc-lang') == 'es':
            login_errors = {'invalid': 'Loggeo invalido recuerde que el sistema es sensible a minusculas y mayusculas.'}
        else:
            login_errors = {'invalid': 'Invalid log remember that the system is case sensitive'}
        return JsonResponse(login_errors)

    return redirect('index')

@login_required
def logout_user(request):
    """
        Logout user session.
    """

    logout(request)
    
    if request.GET.get('lang') == "es":
        info_message_text = """
            Haz
            <span class="popup__span">&nbsp;cerrado&nbsp;</span>
            sesión
            <span class="popup__span">&nbsp;correctamente</span>
        """
    else:
        info_message_text = """
            You
            <span class="popup__span">&nbsp;have&nbsp;</span>
            successfully
            <span class="popup__span">&nbsp;logged</span>
            out
        """
    messages.info(request, info_message_text)

    return redirect(request.GET.get('next'))