from kit.models import Kit
from card.models import Card
from rest_framework import viewsets
from django.utils.decorators import method_decorator

from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import KitSerializer, CardSerializer
from rest_framework import filters

from .custom_permissions import GuestsReadOnly
from .handle_custom_filters.custom_filters import (
                                ByKitAttrFilterBackend,
                                BySuccessfulRangeFilterBackend,
                                ByCardAttrFilterBackend,
                                ByHitsRangeFilterBackend,
                                ByMistakesRangeFilterBackend,
                                BySuccessRangeFilterBackend
                            )
from .custom_schemas.kit_schemas import (
                            kit_list_schema,
                            kit_all_schema,
                            kit_retrieve_schema,
                            kit_create_schema,
                            kit_update_schema,
                            kit_partial_update_schema,
                            kit_destroy_schema
                         )
from .custom_schemas.card_schemas import (
                            card_list_schema,
                            card_all_schema,
                            card_retrieve_schema,
                            card_create_schema,
                            card_update_schema,
                            card_partial_update_schema,
                            card_destroy_schema
                          )


@method_decorator(name='list', decorator=kit_list_schema)
@method_decorator(name='all', decorator=kit_all_schema)
@method_decorator(name='retrieve', decorator=kit_retrieve_schema)
@method_decorator(name='create', decorator=kit_create_schema)
@method_decorator(name='update', decorator=kit_update_schema)
@method_decorator(name='partial_update', decorator=kit_partial_update_schema)
@method_decorator(name='destroy', decorator=kit_destroy_schema)
class KitViewSet(viewsets.ModelViewSet):
    """
    Esta vista permite **ver, crear, modificar y eliminar Kits** para el *usuario actual*.

    Se visualizan maximo 6 kits por pagina.

    ## Acciones

    Use `/all` para ver todos los kits sin paginación.

    ## Filtros

    Puede usar get-parameters para **filtrar por atributo**, por ejemplo.
    > api/kits/?name=kitname

    Tambien por **rango de exito**, con *min_successful* y *max_successful*. Del 0 al 100.
    > api/kits/?min_successful=12&max_successful=80
    
    > api/kits/?min_successful=50
    
    > api/kits/?max_successful=70
    """

    queryset = Kit.objects.all()
    serializer_class = KitSerializer
    permission_classes = [permissions.IsAuthenticated, GuestsReadOnly]
    filter_backends = [
                       filters.SearchFilter,
                       filters.OrderingFilter, 
                       ByKitAttrFilterBackend,
                       BySuccessfulRangeFilterBackend,
                       ]
    search_fields = ['name', 'foreign_language', 'native_language']
    ordering_fields = ['name', 'foreign_language', 'native_language', 'successful']
    ordering = ['name']

    def get_queryset(self):
        """
            Gets Queryset and assigns current user' primary key
        """
        return self.queryset.filter(user__pk = self.request.user.pk)

    def perform_create(self, serializer):
        """
            We override the creation to assign the user to it.
        """
        serializer.save(user=self.request.user)

    def perform_update(self, serializer):
        """
            We override the update to assign the user to it.
        """
        serializer.save(user=self.request.user)

    @action(detail=False, methods=['get'], name='Show all Kits')
    def all(self, request):
        """
            Get all cards of current user without pagination
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"count" : queryset.count(),
                         "results" : serializer.data})


@method_decorator(name='list', decorator=card_list_schema)
@method_decorator(name='all', decorator=card_all_schema)
@method_decorator(name='retrieve', decorator=card_retrieve_schema)
@method_decorator(name='create', decorator=card_create_schema)
@method_decorator(name='update', decorator=card_update_schema)
@method_decorator(name='partial_update', decorator=card_partial_update_schema)
@method_decorator(name='destroy', decorator=card_destroy_schema)
class CardViewSet(viewsets.ModelViewSet):
    """
    Esta vista permite **ver, crear, modificar y eliminar Tarjetas** para el *usuario actual*.

    Se visualizan maximo 6 cards por pagina.

    ## Acciones

    Use `/all` para ver todas las cards sin paginación.

    ## Filtros

    Puede usar get-parameters para **filtrar por atributo**, por ejemplo.
    > api/cards/?foreign_word=someforeignword

    Tambien por **rango de exito**, con *min_success* y *max_success*. Del 0 - 100.
    > api/cards/?min_success=12&max_success=80
    
    > api/cards/?min_success=50
    
    > api/cards/?max_success=70
    
    Tambien por **rango de aciertos**, con *min_hits* y *max_hits*. Con un minimo de 0.
    > api/cards/?min_hits=5&max_hits=17

    Tambien por **rango de errores**, con *min_mistakes* y *max_mistakes*. Con un minimo de 0.
    > api/cards/?min_mistakes=10
    """

    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [permissions.IsAuthenticated, GuestsReadOnly]
    filter_backends = [
                    filters.SearchFilter,
                    filters.OrderingFilter, 
                    ByCardAttrFilterBackend,
                    ByHitsRangeFilterBackend,
                    ByMistakesRangeFilterBackend,
                    BySuccessRangeFilterBackend,
                    ]
    search_fields = ['foreign_word', 'native_word']
    ordering_fields = ['foreign_word', 'native_word', 'hits', 'mistakes', 'success']
    ordering = ['foreign_word']

    def get_queryset(self):
        """
            Gets Queryset and assigns current user' primary key
        """
        return self.queryset.filter(kit__user__pk = self.request.user.pk)

    @action(detail=False, methods=['get'], name='Show all Cards')
    def all(self, request):
        """
            Get all cards of current user without pagination
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response({"count" : queryset.count(),
                         "results" : serializer.data})