from django.shortcuts import render
from django.http import HttpResponse
from app.models import  Person
from app.models import  Admin
from app.models import  Mayor
from app.models  import Request  
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
@method_decorator(login_required(login_url='/login'), name='dispatch') # sur `dispatch` : pour toutes les méthode HTTP(post, get, ...)

class all_demand(TemplateView):
    template_name = "app/municipality/all_demand.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
         #RECUPERATION DES INFO DU USER CONNECTER
        context['person_id']=self.request.user.person_id
        user_connected=Person.objects.get(pk=context['person_id'])    
        context['profil']=user_connected 
        context['user']=self.request.user

        #RECUPERATION DES DEMANDES
        requests_attente=Request.objects.filter(request_status='En attente' )
        requests_invalid=Request.objects.filter(request_status='Non valide' )
        context['request_attente']=requests_attente
        context['request_invalid']=requests_invalid

        return context