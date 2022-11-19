from django.shortcuts import render
from django.http import JsonResponse
from templatetranslation.models import TemplateTranslation

# Create your views here.
def get_translate_template(request, view_name):


    tplt_translation_many = TemplateTranslation.objects.filter(view=view_name)

    if request.user.is_authenticated:
        tplt_translation = tplt_translation_many.filter(is_user_authenticated=True)[0]
    else:
        tplt_translation = tplt_translation_many.filter(is_user_authenticated=False)[0]

    elements_translation = tplt_translation.elementstranslation.values('selector', 'spanish_text', 'english_text')

    return JsonResponse(list(elements_translation), safe=False)
