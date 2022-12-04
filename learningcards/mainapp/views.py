from django.shortcuts import render
from users.forms import SignUpForm, LoginForm

from kit.models import Kit
from kit.forms import AddKit

from .threading_requests_parse_utils import threading_get_imgs

# Create your views here.
def index(request):

    context = {
        'title' : 'Inicio',
        'is_index': True,
    }

    if not request.user.is_authenticated:
        context['signup_form'] = SignUpForm(auto_id="signup_%s")
        context['login_form'] = LoginForm
    else:
        context['kits'] = Kit.objects.filter(user__pk=request.user.pk)
        context['addKit__form'] = AddKit

    if context.get('kits'):
        threading_get_imgs(context['kits'], 'name')

    return render(request, 'mainapp/index.html', context)