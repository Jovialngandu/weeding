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
class historic_mariage(TemplateView):
    template_name = "app/municipality/historic_mariage.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        #RECUPERATION DES INFO DU USER CONNECTER
        context['person_id']=self.request.user.person_id
        user_connected=Person.objects.get(pk=context['person_id'])    
        context['profil']=user_connected


        #RECUPERER  LES MARIAGES QUI ONT EU LIEU
        today = timezone.now().date()  # Obtient la date actuelle
        celebrate_marriages = Marriage.objects.filter(celebration_date__lte=today)
        context['celebrate_mariage']= celebrate_marriages
        




       
        return context