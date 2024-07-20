from django.shortcuts import render
from django.http import HttpResponse
from app.models import  Person
from app.models import  Admin
from app.models import  Mayor  
from django.views.generic import TemplateView

class all_demand(TemplateView):
    template_name = "app/municipality/all_demand.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context