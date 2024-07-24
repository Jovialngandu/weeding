from django.shortcuts import render
from django.http import HttpResponse
from app.models.User import User
from django.views.generic import TemplateView

class home(TemplateView):
    
    template_name ="app/couple/home.html"
   
    def get_queryset(self):
            return  " "
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)      
        return context