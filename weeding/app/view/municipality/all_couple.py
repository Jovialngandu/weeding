from django.shortcuts import render
from django.views.generic import TemplateView
from app.models.Couple import  Couple
from django.http import HttpResponse
from app.models  import Marriage
from app.models  import Person
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
@method_decorator(login_required(login_url='/login'), name='dispatch') # sur `dispatch` : pour toutes les méthode HTTP(post, get, ...)

class couples(TemplateView):
    template_name = "app/municipality/all_couple.html"
   
    def get_queryset(self):
           return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #RECUPERATION DES INFO DU USER CONNECTER
        context['person_id']=self.request.user.person_id
        user_connected=Person.objects.get(pk=context['person_id'])    
        context['profil']=user_connected 
        context['user']=self.request.user
        context["marriage"] = Marriage.objects.all()
        
        
        return context