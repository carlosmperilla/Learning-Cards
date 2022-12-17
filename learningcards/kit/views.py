import json
import random

from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse, HttpResponseNotFound
from django.contrib import messages
from django.db import transaction
from django.urls import reverse
from django.core.paginator import Paginator

from .models import Kit
from .forms import AddKit, EditKit
from card.forms import ValidateForeignWord

from mainapp.threading_requests_parse_utils import threading_get_imgs


# Create your views here.
@login_required
def kit(request, kit_name : str):
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
            'has_previous_page' : cards_page.has_previous(),
            'has_next_page' : cards_page.has_next(),
            'total_pages' : cards_paginator.num_pages,
            'title': kit_by_name.name,
            'is_kit' : True,
            'validateWord__form' : ValidateForeignWord(auto_id=None),
        }

        return render(request, 'kit/kit.html', context)


@login_required
def randomize_kit(request, kit_name : str):
    """
        Reassigns the seed for card shuffling.
    """
    kits = Kit.objects.filter(user__pk=request.user.pk)
    kit_by_name = get_object_or_404(kits, name=kit_name)
    kit_by_name_key = str(kit_by_name)
    
    request.session['seed_card_distribution'][kit_by_name_key] = random.randint(1,1000)
    request.session.modified = True
    
    return JsonResponse({'randomized' : True})

@login_required
def add_kit(request):
    """
        Validate and add a kit.
    """

    if request.method == "POST" and request.user.username == "Invitados":
        if request.POST.get('lc-lang') == "es":
            info_msg = "El modo Invitados, no tiene habilitada esta opción. Regístrese primero."
        else:
            info_msg = "Guest mode does not have this option enabled. Sign up first."
        messages.info(request, info_msg)
        return redirect("index")

    if request.method == "POST":
        message_error = None
        message_success = None
        add_kit_form = AddKit(request.POST, request.FILES)
        if add_kit_form.is_valid():
            kit = Kit(
                name = request.POST.get('name'),
                foreign_language = request.POST.get('foreign_language'),
                native_language = request.POST.get('native_language'),
                user = request.user
                )
            kit.lc_lang = request.POST.get('lc-lang')
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

                if e.messages[0].startswith('UNPS'):
                    message_error = e.messages[0].replace('UNPS - ', '')
                else:
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
    """
        Edit the name, foreign language, and native language of one or more kits.
    """
    
    data = {"redirect_url" : reverse('index')}
    edited_kits_data = json.loads(request.body)
    lc_lang = edited_kits_data.pop("lc-lang")
    
    if request.method == "POST" and request.user.username == "Invitados":
        if lc_lang == "es":
            info_msg = "El modo Invitados, no tiene habilitada esta opción. Regístrese primero."
        else:
            info_msg = "Guest mode does not have this option enabled. Sign up first."
        messages.info(request, info_msg)
        return JsonResponse(data)

    if request.method == "POST":
        editable_fields = ['foreign_language', 'native_language', 'name']
        kits_by_user = Kit.objects.filter(user__pk=request.user.pk)
        with transaction.atomic():
            for id, edited_fields in edited_kits_data.items():
                try:
                    kit = kits_by_user.filter(id=int(id.replace("kit-", "")))
                    valid_edited_fields = {key:value for key, value in edited_fields.items() if key in editable_fields}
                    if kit[0].name != valid_edited_fields.get('name', kit[0].name):
                        if kits_by_user.filter(name=valid_edited_fields['name']).exists():
                            if lc_lang == "es":
                                raise ValidationError("UNPS - Nombre de Kit ya registrado previamente.")
                            else:
                                raise ValidationError("UNPS - Kit name already registered previously.")
                    form = EditKit(valid_edited_fields)
                    if form.is_valid():
                        kit.update(**valid_edited_fields)
                    else:
                        raise ValidationError('Edición no valida')
                except Exception as e:
                    print(e)
                    import traceback
                    traceback.print_exc()

                    if e.messages[0].startswith('UNPS'):
                        error_msg = e.messages[0].replace('UNPS - ', '')
                    else:
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
    """
        Delete one to several kits.
    """

    data = {"redirect_url" : reverse('index')}
    delete_data = json.loads(request.body)
    lc_lang = delete_data.pop("lc-lang")
    
    if request.method == "POST" and request.user.username == "Invitados":
        if lc_lang == "es":
            info_msg = "El modo Invitados, no tiene habilitada esta opción. Regístrese primero."
        else:
            info_msg = "Guest mode does not have this option enabled. Sign up first."
        messages.info(request, info_msg)
        return JsonResponse(data)

    if request.method == "POST":
        kits_by_user = Kit.objects.filter(user__pk=request.user.pk)
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
