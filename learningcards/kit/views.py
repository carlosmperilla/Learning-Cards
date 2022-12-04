import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, HttpResponseNotFound
from django.contrib import messages
from django.db import transaction
from django.urls import reverse

from .models import Kit
from .forms import AddKit
from card.forms import ValidateForeignWord

from mainapp.threading_requests_parse_utils import threading_get_imgs
import random

from django.core.paginator import Paginator

# Create your views here.
@login_required
def kit(request, kit_name):
    """
        Render the kit in template.
    """

    if request.method == "GET":
        kits = Kit.objects.filter(user__pk=request.user.pk)
        kit_by_name = get_object_or_404(kits, name=kit_name)
        kit_by_name_key = str(kit_by_name)
        cards_by_kit = kit_by_name.cards.all()
        page_num = 1

        if not request.session.get('seed_card_distribution'):
            request.session['seed_card_distribution'] = {}
        
        if not request.session['seed_card_distribution'].get(kit_by_name_key):
            request.session['seed_card_distribution'][kit_by_name_key] = random.randint(1,1000)
            request.session.modified = True

        if request.GET.get('page'):
            if not request.GET.get('page').isdigit():
                return HttpResponseNotFound()    
            page_num = int(request.GET.get('page'))

        l_cards = list(cards_by_kit)
        random.seed(request.session.get('seed_card_distribution')[kit_by_name_key])
        random.shuffle(l_cards)
        random.seed(None) #reset random

        cards_paginator = Paginator(l_cards, 6)

        if (page_num > cards_paginator.num_pages) or (page_num < 1):
            return HttpResponseNotFound()
        
        cards_page = cards_paginator.page(page_num)
        
        if cards_page:
            threading_get_imgs(cards_page, 'foreign_word')

        l_cards_page = list(cards_page)


        context = {
            'kits' : kits,
            'kit' : kit_by_name,
            'cards' : l_cards_page,
            # 'current_page' : page_num,
            'has_previous_page' : cards_page.has_previous(),
            'has_next_page' : cards_page.has_next(),
            'total_pages' : cards_paginator.num_pages,
            'title': kit_by_name.name,
            'is_kit' : True,
            'validateWord__form' : ValidateForeignWord(auto_id=None),
        }

        return render(request, 'kit/kit.html', context)


@login_required
def randomize_kit(request, kit_name):
    kits = Kit.objects.filter(user__pk=request.user.pk)
    kit_by_name = get_object_or_404(kits, name=kit_name)
    kit_by_name_key = str(kit_by_name)
    
    request.session['seed_card_distribution'][kit_by_name_key] = random.randint(1,1000)
    request.session.modified = True
    
    return JsonResponse({'randomized' : True})

@login_required
def add_kit(request):

    if request.method == "POST":
        message_error = None
        add_kit_form = AddKit(request.POST, request.FILES)
        if add_kit_form.is_valid():
            kit = Kit(
                name = request.POST.get('name'),
                foreign_language = request.POST.get('foreign_language'),
                native_language = request.POST.get('native_language'),
                user = request.user
                )
            try:
                kit.full_clean()
                kit.save()
                kit.generate_cards(request.FILES.get('kit_file'))
                if request.POST.get('lc-lang') == "es":
                    message_success = "¡Kit añadido correctamente!"
                else:
                    message_success = "Kit added successfully!"
            except Exception as e:
                print(e)
                import traceback
                traceback.print_exc()
                if request.POST.get('lc-lang') == "es":
                    message_error = "Formato de Kit invalido, vuelva a intentarlo"
                else:
                    message_error = "Kit format invalid, try again"
        else:
            if request.POST.get('lc-lang') == "es":
                message_error = "Formulario invalido, vuelva a intentarlo"
            else:
                message_error = "Invalid form, try again"

        if message_error:
            messages.error(request, message_error)

        if message_success:
            messages.success(request, message_success)


    return redirect("index")

@login_required
def edit_kits(request):

    if request.method == "POST":
        data = {"redirect_url" : reverse('index')}
        kits_by_user = Kit.objects.filter(user__pk=request.user.pk)
        edited_kits_data = json.loads(request.body)
        lc_lang = edited_kits_data.pop("lc-lang")
        with transaction.atomic():
            for id, edited_fields in edited_kits_data.items():
                try:
                    kit = kits_by_user.filter(id=int(id.replace("kit-", "")))
                    kit.update(**edited_fields)
                except Exception as e:
                    print(e)
                    import traceback
                    traceback.print_exc()
                    if lc_lang == "es":
                        error_msg = "Ha existido un problema en la edición. Vuelva a intentarlo."
                    else:
                        error_msg = "There was a problem in editing. Try again."
                    messages.error(request, error_msg)
                    return JsonResponse(data)

        if lc_lang == "es":
            success_msg = "Edición realizada correctamente!"
        else:
            success_msg = "Editing done successfully!"
        messages.success(request, success_msg)
        return JsonResponse(data)

@login_required
def delete_kits(request):
    if request.method == "POST":
        data = {"redirect_url" : reverse('index')}
        kits_by_user = Kit.objects.filter(user__pk=request.user.pk)
        delete_data = json.loads(request.body)
        lc_lang = delete_data.pop("lc-lang")
        kits_to_delete_ids = [int(kit_id.replace("kit-", "")) for kit_id in delete_data['kitsToDelete']]
        try:
            kits_by_user.filter(id__in=kits_to_delete_ids).delete()
        except Exception as e:
            print(e)
            import traceback
            traceback.print_exc()
            if lc_lang == "es":
                error_msg = "Ha existido un problema en la eliminación. Vuelva a intentarlo."
            else:
                error_msg = "There was a problem in deleting. Try again."
            messages.error(request, error_msg)
            return JsonResponse(data)

        if lc_lang == "es":
            success_msg = "Elimación realizada correctamente!"
        else:
            success_msg = "Deleting done successfully!"
        messages.success(request, success_msg)
        return JsonResponse(data)
