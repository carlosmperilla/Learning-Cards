from django.shortcuts import render
from users.forms import SignUpForm, LoginForm


# Create your views here.
def index(request):


    context = {
        'title' : 'Inicio',
        'signup_form' : SignUpForm(auto_id="signup_%s"),
        'login_form' : LoginForm,
    }

    return render(request, 'mainapp/index.html', context)