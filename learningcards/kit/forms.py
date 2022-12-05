from django import forms
from django.forms import ModelForm, ValidationError
from .models import Kit


class AddKit(ModelForm):
    class Meta:
        model = Kit
        fields = ('name', 'foreign_language', 'native_language')
        labels = {
            'name' : 'Nombre de Kit',
            'foreign_language' : 'Lenguaje a aprender',
            'native_language' : 'Lenguaje nativo',
        }
    
    kit_file = forms.FileField(required=True, label = "Archivo de vocabulario")

    def __init__(self, *args, **kwargs):
        super(AddKit, self).__init__(*args, **kwargs)

        self.fields['kit_file'].widget.attrs.update({
                                                        'accept': '.txt',
                                                        })

    def clean_kit_file(self):
        data = self.cleaned_data['kit_file']
        if data:
            if not data.name.endswith('.txt'):
                raise ValidationError(f"No es un archivo de texto")
            if data.size >  (1 * (1024**2)): #1 MB
                raise ValidationError(f"El vocabulario es demasiado extenso.")
            
        return data

class EditKit(ModelForm):
    class Meta:
        model = Kit
        fields = ('name', 'foreign_language', 'native_language')

    def __init__(self, *args, **kwargs):
        super(EditKit, self).__init__(*args, **kwargs)
        for key, field in self.fields.items():
            self.fields[key].required = False