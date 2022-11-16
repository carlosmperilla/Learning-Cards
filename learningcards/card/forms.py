from django.forms import ModelForm
from .models import Card

class ValidateForeignWord(ModelForm):
    class Meta:
        model = Card
        fields = ('native_word',)
