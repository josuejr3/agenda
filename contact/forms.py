from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone_number'
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        # print(cleaned_data)

        # Criando um erro
        self.add_error(
            'first_name',
            ValidationError(
                'Mensagem de Erro',
                code='invalid'
            )
        )

        return super().clean()