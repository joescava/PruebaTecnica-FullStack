from django import forms
from .models import ArchivoSubido

class ArchivoForm(forms.ModelForm):
    class Meta:
        model = ArchivoSubido
        fields = ["archivo"]