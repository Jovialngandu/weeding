from django.shortcuts import render
from django.http import HttpResponse
from app.models.Witness import  Witness
from django.views.generic import TemplateView
from app.models  import Person
from app.models  import Marriage
from django.utils import timezone

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='/login'), name='dispatch') # sur `dispatch` : pour toutes les méthode HTTP(post, get, ...)
class update_couple(TemplateView):
    template_name = "app/municipality/update_couple.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        #RECUPERATION DES INFO DU USER CONNECTER
        context['person_id']=self.request.user.person_id
        user_connected=Person.objects.get(pk=context['person_id'])    
        context['profil']=user_connected
    
        return context