from django.shortcuts import render
from users.forms import SignUpForm, LoginForm

from kit.models import Kit
from kit.forms import AddKitTwo

import requests
from bs4 import BeautifulSoup as bs 
from random import randint

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
        context['addKit__form'] = AddKitTwo

    if context.get('kits'):
        for kit in context['kits']:
            url_kit_name = requests.utils.quote(kit.name)
            url_g_img = f"https://www.google.com/search?q={url_kit_name}&tbm=isch&tbs=isz:l"
            g_req = requests.get(url_g_img)
            g_parser = bs(g_req.content, 'html.parser')
            kit.img = g_parser.findAll("img")[randint(1,20)]["src"]

    return render(request, 'mainapp/index.html', context)