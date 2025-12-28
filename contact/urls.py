"""
URL configuration for agenda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from contact import views

app_name = 'contact'

urlpatterns = [
    # Na página raiz do site ele vai chamar a view index "resposta"
    path("", views.index, name="index"),
    # O parâmetro da request é obtido pelo primeiro argumento da path - READ
    path("contact/<int:contact_id>/detail/", views.contact, name="contact"),
    # CREATE
    path("contact/create/", views.create, name="create"),
    # DELETE
    path("contact/<int:contact_id>/delete/", views.delete, name="delete"),
    # UPDATE
    path("contact/<int:contact_id>/update/", views.update, name="update"),
    path("search/", views.search, name="search"),


    # URLs para Users
    path('user/create/', views.register, name='register'),


]
