from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.http import Http404
from django.db.models import Q

# Create your views here.

def index(request):

    # normalmente não usamos o all
    contacts = Contact.objects.all().order_by('-id').filter(show=True)[0:10]
    # filter faz o filtro do que vai ser selecionado
    # Vendo a consulta que está sendo feita no terminal
    # print(contacts.query)

    context = {
        'contacts': contacts,
        'site_tile': "Contatos - "
    }

    return render(
        request,
        'contact/index.html',
        context
    )

def search(request):

    search_value = request.GET.get('query', '').strip()
    print(search_value)

    # Se for uma consulta inválida ele volta pra index
    if search_value == '':
        return redirect('contact:index')

    # consultas em que é feito o uso da "," e dos parâmetros é basicamente um AND
    contacts = Contact.objects.filter(show=True).filter(
        Q(first_name__icontains=search_value) |
        Q(last_name__icontains=search_value)
    ).order_by('-id')

    print(contacts.query)

    context = {
        'contacts': contacts,
        'site_tile': "Search - "
    }

    return render(
        request,
        'contact/index.html',
        context
    )


def contact(request, contact_id):

    # Fazendo busca com get
    # single_contact = Contact.objects.get(pk=contact_id)

    # Para evitar erro de procurar u elemento fora do range eu poderia usar
    # single_contact = Contact.objects.filter(pk=contact_id).first()

    # Outra opção usando a função get_object_or_404
    single_contact = get_object_or_404(
        Contact,
        id=contact_id,
        show=True
    )

    site_title = f"{single_contact.first_name} {single_contact.last_name} - "

    context = {
        'contact': single_contact,
        'site_title': site_title
    }

    return render(
        request,
        "contact/contact.html",
        context
    )