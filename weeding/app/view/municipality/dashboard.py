
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

class dashboard(TemplateView):
    template_name = "app/municipality/dashboard.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context