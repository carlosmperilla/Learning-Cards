from django.http import JsonResponse
from templatetranslation.models import TemplateTranslation
from django.views import View

# Create your views here.
class GetTranslateTemplate(View):
    """
        Get the elements in Spanish and English. Filtering by its view and authentication.
    """

    def post(self, request, *args, **kwargs):
        tplt_translation_many = TemplateTranslation.objects.filter(view=self.kwargs['view_name'])
        tplt_translation = tplt_translation_many.filter(is_user_authenticated=request.user.is_authenticated)[0]
        elements_translation = tplt_translation.elementstranslation.values('selector', 'spanish_text', 'english_text', 'multiple')

        return JsonResponse(list(elements_translation), safe=False)