import json

from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from django.db import transaction
from django.urls import reverse

from .models import Kit
from .forms import AddKit

# Create your views here.
@login_required
def kit(request, kit_name):
    """
        Render the kit in template.
    """
    kits = Kit.objects.filter(user__pk=request.user.pk)
    kit_by_name = get_object_or_404(kits, name=kit_name)
    cards_by_kit = kit_by_name.cards.all()

    context = {
        'kits' : kits,
        'kit' : kit_by_name,
        'cards' : cards_by_kit,
        'mode' : 0
    }

    if request.GET.get("mode"):
        pass
        # context["mode"] = int(request.GET.get("mode"))

        # if context["mode"] == 1:
        #     context['form_import_images'] = ImportImages()

    # return render(request, "stock/stock.html", context)
    return HttpResponse(kit_by_name.name)

@login_required
def add_kit(request):

    if request.method == "POST":
        message_error = None
        print(request.POST.get('kit_file'))
        print(request.FILES)
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