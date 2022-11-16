from django import forms
from django.forms import ModelForm, ValidationError
from .models import Kit

class AddKit(forms.Form):
    kit_file = forms.ClearableFileInput(required=True)

    def clean_kit_file(self):
        data = self.cleaned_data['kit_file']
        if data:
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