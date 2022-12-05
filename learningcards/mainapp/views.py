from django.views.generic.base import TemplateView
from users.forms import SignUpForm, LoginForm

from kit.models import Kit
from kit.forms import AddKit

from .threading_requests_parse_utils import threading_get_imgs

# Create your views here.
class IndexPageView(TemplateView):
    """
        Render the index template.
    """

    template_name = "mainapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'title' : 'Inicio',
            'is_index': True,
        })

        if not self.request.user.is_authenticated:
            context['signup_form'] = SignUpForm(auto_id="signup_%s")
            context['login_form'] = LoginForm
        else:
            context['kits'] = Kit.objects.filter(user__pk=self.request.user.pk)
            context['addKit__form'] = AddKit
            threading_get_imgs(context['kits'], 'name')
        
        return context
