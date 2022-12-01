from django import forms
from django.forms import ModelForm, ValidationError
from .models import Kit


class AddKitTwo(ModelForm):
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
        super(AddKitTwo, self).__init__(*args, **kwargs)

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


class AddKit(forms.Form):
    kit_file = forms.FileField(required=True, label = "Archivo de vocabulario")

    def __init__(self, *args, **kwargs):
        super(AddKit, self).__init__(*args, **kwargs)

        for field in self.fields:   
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

class EditNameKit(ModelForm):
    class Meta:
        model = Kit
        fields = ('name',)
        labels = {
            'name' : 'Nombre de Kit',
        }

class DeleteKit(forms.Form):
    password = forms.CharField(
                                required=True,
                                label = "Contraseña de Usuario",
                                widget=forms.PasswordInput(
                                    attrs={'type':'password', 'name': 'password','placeholder':'Contraseña de Usuario', 'tabindex' : '1'}
                                    )
                                )