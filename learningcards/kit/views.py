from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Kit

# Create your views here.
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