from django import forms
from .models import PQRS

class Formulariopqrs(forms.ModelForm):
    class Meta:
        model = PQRS
        fields = ('texto', 'opcion',)