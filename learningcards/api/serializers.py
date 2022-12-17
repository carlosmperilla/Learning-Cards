from kit.models import Kit
from card.models import Card
from rest_framework import serializers

from django.db import transaction
from django.core.exceptions import ValidationError

class KitSerializerMin(serializers.HyperlinkedModelSerializer):
    """
        Minimized kit, no cards.
    """
    id = serializers.IntegerField(required=False)
    name=serializers.CharField(required=False)
    class Meta:
        model = Kit
        fields = ['id', 'url', 'name', 'foreign_language', 'native_language', 'successful']
        read_only_fields = ['foreign_language', 'native_language', 'successful', 'id']

class CardSerializerMin(serializers.HyperlinkedModelSerializer):
    """
        Minimized card, no kit.
    """
    id = serializers.IntegerField(required=False)
    class Meta:
        model = Card
        fields = ['id', 'url', 'foreign_word', 'native_word', 'hits', 'mistakes', 'success']
        read_only_fields = ['hits', 'mistakes', 'success', 'id']

class KitSerializer(serializers.HyperlinkedModelSerializer):
    """
        Kit serializer class
    """
    
    cards = CardSerializerMin(read_only = False, many=True, required=False)

    class Meta:
        model = Kit
        fields = ['id', 'url', 'name', 'foreign_language', 'native_language', 'successful', 'cards']
        read_only_fields = ['successful', 'id']

    def create(self, validated_data):
        """
            Behavior for nested objects:
            - If the card field is not sent, the kit is created empty.
            - Cards with a repeated foreign_word are ignored.

            Errors:
            - If the Kit already exists for the current user it raises a ValidationError.
        """
        
        dict_cards = validated_data.pop('cards', [])
        
        try:
            instance = Kit.objects.create(**validated_data)
            cards = []
        
            foreign_words = []
            for dict_card in dict_cards:
                if dict_card.get('foreign_word') in foreign_words:
                    continue
                foreign_words.append(dict_card.get('foreign_word'))
                cards.append(Card(kit = instance, **dict_card))
        
            Card.objects.bulk_create(cards)
        
            return instance
        except ValidationError as e:
            raise serializers.ValidationError({'kit' : 'Nombre de Kit ya registrado previamente.'})


    def update(self, instance, validated_data):
        """
            Behavior for nested objects:
            - If the card field is not sent, the previous state of the cards remains unchanged.
            - Cards with a repeated foreign_word are ignored.
            - Cards that are not sent are removed, since the cards object is sent complete.
            - Cards that do not have an id are created.

            Errors:
            - If the Kit already exists for the current user it raises a ValidationError.
        """

        dict_cards = validated_data.pop('cards', None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        try:
            instance.save()
        except ValidationError as e:
            raise serializers.ValidationError({'kit' : 'Nombre de Kit ya registrado previamente.'})


        if dict_cards != None:
            id_cards = []
            cards_in_kit = instance.cards.all()

            try:
                foreign_words = []
                with transaction.atomic():
                    for dict_card in dict_cards:
                        
                        if dict_card.get('foreign_word') in foreign_words:
                            if 'id' in dict_card: #Evita la perdida de información.
                                card_id = dict_card.pop('id')
                                id_cards.append(card_id)
                            continue
                        foreign_words.append(dict_card.get('foreign_word'))
                        
                        if 'id' in dict_card:
                            card_id = dict_card.pop('id')
                            id_cards.append(card_id)
                            cards_in_kit.filter(id=card_id).update(**dict_card)
                        else:
                            new_card = Card(kit = instance, **dict_card)
                            new_card.save()
                            id_cards.append(new_card.id)
            except Exception as e:
                print(e)
            else:
                cards_in_kit.exclude(id__in=id_cards).delete()

        return instance


class CardSerializer(serializers.HyperlinkedModelSerializer):
    """
        Card serializer class
    """

    kit = KitSerializerMin(read_only = False, required = False)

    class Meta:
        model = Card
        fields = ['id', 'url', 'foreign_word', 'native_word', 'hits', 'mistakes', 'success', 'kit']
        read_only_fields = ['hits', 'mistakes', 'success', 'id', 'kit']

    def get_fields(self, *args, **kwargs): #Para modificar propiedades dinamicamente
        """
            Behavior for nested objects:
            - The kit cannot be modified by its cards. It's read-only.
        
        """
        fields = super(CardSerializer, self).get_fields(*args, **kwargs)
        request = self.context.get('request', None)
        if request and getattr(request, 'method', None) == "PUT":
            fields['kit'].required = False
            fields['kit'].read_only = True
        return fields

    def create(self, validated_data):
        """
            Behavior for nested objects:
            - The kit must be sent, with your name or id.

            Errors:
                ValidationsError in case of:
                - If the kit does not meet the specifications.
                - If there is already a card with that foreign_word.
        """
        dict_kit = validated_data.pop('kit', [])

        if dict_kit:
            user_pk = self.context['request'].user.pk
            kit_id = dict_kit.get('id')
            kit_name = dict_kit.get('name')
            
            if kit_id:
                kit = Kit.objects.filter(user__pk=user_pk).filter(pk=kit_id)
            
            if kit_name:
                kit = Kit.objects.filter(user__pk=user_pk).filter(name=kit_name)

            if not kit.exists():
                raise serializers.ValidationError("El kit no existe o no pertenece al usuario actual")

            if kit[0].cards.filter(foreign_word=validated_data.get('foreign_word')).exists():
                raise serializers.ValidationError("Ya existe una tarjeta en este kit con esa palabra foranea.")

            instance = Card.objects.create(kit=kit[0], **validated_data)
            return instance
        else:
            raise serializers.ValidationError({"kit": "El id o el nombre del kit, son obligatorios"})

    def update(self, instance, validated_data):
        """
            Behavior for nested objects:
            - The kit is removed.

            Errors:
                ValidationsError in case of:
                - If there is already a card with that foreign_word.
        """
        validated_data.pop('kit', None)

        if instance.kit.cards.exclude(pk=instance.pk).filter(foreign_word=validated_data.get('foreign_word')).exists():
            raise serializers.ValidationError("Ya existe una tarjeta en este kit con esa palabra foranea.")

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance