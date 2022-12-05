import json

from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.http import JsonResponse

from kit.models import Kit


class CardJsonHandling(LoginRequiredMixin, View):
    """
        It handles the JSON data and gets the kit and its corresponding card.
    """

    def post(self, request, *args, **kwargs):
        self.data = json.loads(request.body)
        card_id = int(self.data['card_id'].replace('card-', ''))
        kits = Kit.objects.filter(user__pk=request.user.pk)
        self.kit_by_name = get_object_or_404(kits, name=self.kwargs['kit_name'])
        self.card = get_object_or_404(self.kit_by_name.cards, pk = card_id)
        self.json_data = {}

        self.actions(request, *args, **kwargs)

        return JsonResponse(self.json_data)

    def actions(self, request, *args, **kwargs):
        """
            Perform data management actions.
        """
        pass