from django.shortcuts import render
from contact.models import Contact

# Create your views here.

def index(request):

    # normalmente não usamos o all
    contacts = Contact.objects.all().order_by('-id').filter(show=True)[0:10]
    # filter faz o filtro do que vai ser selecionado
    # Vendo a consulta que está sendo feita no terminal
    # print(contacts.query)

    context = {
        'contacts': contacts,
    }

    return render(
        request,
        'contact/index.html',
        context
    )

