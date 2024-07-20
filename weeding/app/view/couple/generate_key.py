from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse

class generate_key(TemplateView):
    template_name ="app/couple/generate_key.html"
   
    def get_queryset(self):
            return  "ceci est la clé"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] = self.get_queryset()
       
        return context