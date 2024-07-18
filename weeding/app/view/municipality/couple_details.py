from django.shortcuts import render
from django.http import HttpResponse
from app.models.Couple import Couple
from django.views.generic import TemplateView

class couple_details(TemplateView):
    template_name = "app/municipality/couple_details.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context