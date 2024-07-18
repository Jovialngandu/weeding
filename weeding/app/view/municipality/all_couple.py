from django.shortcuts import render
from django.views.generic import TemplateView
from app.models.Couple import  Couple
from django.http import HttpResponse

class couples(TemplateView):
    template_name = "app/municipality/all_couple.html"
   
    def get_queryset(self):
            return Couple.objects.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["couples"] = self.get_queryset()
        # print(context)
        return context