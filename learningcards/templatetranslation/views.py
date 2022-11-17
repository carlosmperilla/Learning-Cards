from django.shortcuts import render
from django.http import JsonResponse
from templatetranslation.models import TemplateTranslation
from django.core import serializers

# Create your views here.
def get_translate_template(request, view_name):

    tplt_translation = TemplateTranslation.objects.filter(view=view_name)[0]
    elements_translation = tplt_translation.elementstranslation.values('selector', 'spanish_text', 'english_text')

    return JsonResponse(list(elements_translation), safe=False)
