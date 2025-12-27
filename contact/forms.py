from django import forms
from django.core.exceptions import ValidationError
from . import models

class ContactForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Outra forma sem usar o widget diretamente
        self.fields['first_name'].widget.attrs.update(
            {'placeholder': 'First Name',
             }
        )

        # Inserindo help text
        self.fields['first_name'].help_text = 'Enter your first name'


        self.fields['last_name'].widget.attrs.update(
            {'placeholder': 'Last Name', }
        )

        self.fields['last_name'].help_text = 'Enter your last name'


        self.fields['phone_number'].widget.attrs.update(
            {'placeholder': 'Phone Number',
             'label': 'Phone Number',}
        )

        self.fields['phone_number'].help_text = 'Enter your phone number'




    class Meta:
        model = models.Contact
        fields = (
            'first_name', 'last_name', 'phone_number'
        )

        # Altera o tipo da entrada de texto para password, poderia ser um TextArea também
        # widgets = {
        #     'first_name': forms.TextInput(
        #         # O attrs são atributos do campo, classe, placeholder..
        #         attrs={
        #             'placeholder': 'First Name',
        #             # 'maxlength': 50,
        #         }
        #     ),
        # }

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