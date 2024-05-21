from datetime import date

from django import forms
from .models import Pet


class PetForm(forms.ModelForm):
    class Meta:
        model = Pet
        exclude = ['owner']
        widgets = {
            'birth_date': forms.DateInput(
                format='%d.%m.%Y',
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Дата народження',
                    'type': 'date',
                    'max': date.today(),
                },
            ),
        }
