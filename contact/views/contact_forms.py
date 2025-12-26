from django.shortcuts import render, get_object_or_404, redirect
from contact.models import Contact
from django.db.models import Q
from django import forms
from django.core.exceptions import ValidationError

from contact.forms import ContactForm

# Create your views here.

def create(request):

    if request.method == 'POST':
        # O que passamos para o get é o nome do input que queremos
        #print(request.POST.get('first_name'))
        context = {'form': ContactForm(request.POST)}
        return render(request, 'contact/create.html', context)

    context = {'form': ContactForm()}

    return render(request,'contact/create.html', context)