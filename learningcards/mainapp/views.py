from django.shortcuts import render
from users.forms import SignUpForm, LoginForm

from kit.models import Kit

# Create your views here.
def index(request):

    context = {
        'title' : 'Inicio',
    }

    if not request.user.is_authenticated:
        context['signup_form'] = SignUpForm(auto_id="signup_%s")
        context['login_form'] = LoginForm
    else:
        context['kits'] = Kit.objects.filter(user__pk=request.user.pk)


    return render(request, 'mainapp/index.html', context)