from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.decorators import login_required


from django.urls import reverse

from contact.forms import ContactForm

# Create your views here.
@login_required(login_url='contact:login')
def update(request, contact_id):

    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)

    form_action = reverse('contact:update', args=(contact_id,))

    if request.method == 'POST':

        # A instância informa que os dados ja estao salvos, o que estiver no POST é para atualizar
        form = ContactForm(request.POST, request.FILES, instance=contact)

        context = {
            'form': form,
            'form_action': form_action,
        }

        # Só retorna true se o form não tiver NENHUM erro
        if form.is_valid():
            contact = form.save()
            return redirect('contact:update', contact_id = contact.id)

        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm(instance=contact),
        'form_action': form_action,
    }

    return render(request,'contact/create.html', context)


@login_required(login_url='contact:login')
def create(request):

    form_action = reverse('contact:create')

    if request.method == 'POST':
        # O que passamos para o get é o nome do input que queremos
        #print(request.POST.get('first_name'))

        form = ContactForm(request.POST, request.FILES)

        context = {
            'form': form,
            'form_action': form_action,
        }

        # Só retorna true se o form não tiver NENHUM erro
        if form.is_valid():
            contact = form.save(commit=False)
            contact.owner = request.user
            contact.save()
            return redirect('contact:update', contact_id = contact.id)

        return render(request, 'contact/create.html', context)

    context = {
        'form': ContactForm(),
        'form_action': form_action,
    }

    return render(request,'contact/create.html', context)


@login_required(login_url='contact:login')
def delete(request, contact_id):

    contact = get_object_or_404(Contact, pk=contact_id, show=True, owner=request.user)
    # contact.delete()
    # return redirect('contact:index')

    confirmation = request.POST.get('confirmation', 'no')

    if confirmation == 'yes':
        contact.delete()
        return redirect('contact:index')

    return render(request, 'contact/contact.html',
                  {'contact': contact, 'confirmation': confirmation})