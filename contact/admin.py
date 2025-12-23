from django.contrib import admin

from contact.models import Contact, Category


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = "name",
    ordering = "name",

# Configuração da Admin de Contact no Django
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = 'id', 'first_name', 'last_name', 'phone_number', 'category'
    ordering = '-id',
    # list_filter = 'created_date',
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200
    # list_editable = 'first_name', 'last_name',
    list_display_links = 'id', 'phone_number',

