from django.shortcuts import render
from django.views.generic import ListView
from contact.models import Profile

class Contact(ListView):
    model = Profile
    template_name = "contact.html"
