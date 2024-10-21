from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class Register(TemplateView):
    template_name = "register.html"

class login(TemplateView):
    template_name = "login.html"


class grabe(TemplateView):
    template_name = "grabe.html"

class home(TemplateView):
    template_name = "home.html"


class raspisania(TemplateView):
    template_name = "raspisania.html"

class profile(TemplateView):
    template_name = "profile.html"