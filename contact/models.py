from django.db import models
from django.utils import timezone

# Create your models here.

# Model de Contato

class Contact(models.Model):

    # Dados do Contato, o blank deixa como opcional

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)

    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'



