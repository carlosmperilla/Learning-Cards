import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from mainapp.threading_requests_parse_utils import buil_url, get_img_google
from kit.models import Kit
from .forms import ValidateForeignWord


# Create your views here.
@login_required
def show_native_word(request, kit_name):

    if request.method == "POST":
        data = json.loads(request.body)
        kits = Kit.objects.filter(user__pk=request.user.pk)
        kit_by_name = get_object_or_404(kits, name=kit_name)
        card_id = int(data['card_id'].replace('card-', ''))
        card = get_object_or_404(kit_by_name.cards, pk = card_id)

        json_data = {
            'native_word' : card.native_word,
        }

        return JsonResponse(json_data)

@login_required
def replace_img(request, kit_name):

    if request.method == "POST":
        data = json.loads(request.body)
        kits = Kit.objects.filter(user__pk=request.user.pk)
        kit_by_name = get_object_or_404(kits, name=kit_name)
        card_id = int(data['card_id'].replace('card-', ''))
        card = get_object_or_404(kit_by_name.cards, pk = card_id)

        url_img = buil_url(card, 'foreign_word')
        get_img_google(card, url_img)

        json_data = {
            'url_img' : card.img,
        }

        return JsonResponse(json_data)

@login_required
def check_answer(request, kit_name):
    if request.method == "POST":
        data = json.loads(request.body)
        kits = Kit.objects.filter(user__pk=request.user.pk)
        kit_by_name = get_object_or_404(kits, name=kit_name)
        card_id = int(data['card_id'].replace('card-', ''))
        card = get_object_or_404(kit_by_name.cards, pk = card_id)

        json_data = {
                'passed' : False,
            }
        form = ValidateForeignWord({'native_word': data['native_word']})
        if form.is_valid():
            is_passed = data["native_word"].lower().split() == card.native_word.lower().split()
            json_data['passed'] = is_passed
        
        if json_data['passed']:
            card.hits += 1
            json_data['hits'] = card.hits
        else:
            card.mistakes += 1
            json_data['mistakes'] = card.mistakes
        
        card.put_success()
        kit_by_name.put_successful()
        json_data['progress'] = kit_by_name.successful

        return JsonResponse(json_data)