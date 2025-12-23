from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

# Model Category

class Category(models.Model):

    # Essa classe serve para modificar o nome do plural de category no admin
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.name}"

# Model de Contato

class Contact(models.Model):

    # Dados do Contato, o blank deixa como opcional

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(max_length=254, blank=True)

    created_date = models.DateTimeField(default=timezone.now)
    description = models.TextField(blank=True)

    show = models.BooleanField(default=True)
    picture = models.ImageField(blank=True, upload_to="pictures/%Y/%m/")

    # O on_delate é basicamente o que vai acontecer se a categoria for excluida
    # cascade - apaga em cascata
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True)

    owner = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.first_name} {self.last_name}'

