from django.shortcuts import render
from django.http import HttpResponse
from app.models import  Admin 
from app.models.Witness import  Witness
from django.views.generic import TemplateView

class connexion(TemplateView):
    template_name = "app/couple/couple_login.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context