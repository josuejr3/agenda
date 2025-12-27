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
            'first_name', 'last_name', 'phone_number',
            'email', 'description', 'category',
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
        first_name = cleaned_data.get('first_name')
        last_name = cleaned_data.get('last_name')

        if first_name == last_name:
            msg = ValidationError(
                'Primeiro nome não pode ser igual ao segundo',
                code='invalid'
            )

            self.add_error('first_name', msg)
            self.add_error('last_name', msg)

        return super().clean()

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')

        if first_name == 'ABC':
            self.add_error(
                'first_name',
                ValidationError(
                    'Veio do add_error',
                    code='invalid'
                )
            )

        return first_name