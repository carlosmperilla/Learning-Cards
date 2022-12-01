from django.shortcuts import render
from django.http import JsonResponse
from templatetranslation.models import TemplateTranslation

# Create your views here.
def get_translate_template(request, view_name):

    if request.method == "POST":
        tplt_translation_many = TemplateTranslation.objects.filter(view=view_name)
        tplt_translation = tplt_translation_many.filter(is_user_authenticated=request.user.is_authenticated)[0]
        elements_translation = tplt_translation.elementstranslation.values('selector', 'spanish_text', 'english_text', 'multiple')

        return JsonResponse(list(elements_translation), safe=False)
