from django.shortcuts import render
from django.http import HttpResponse
from app.models.Couple import Couple
from app.models.Couple import Person
from app.models.Marriage import Marriage
from app.models.Witness import Witness
from app.models import Officer
from django.views.generic import TemplateView

class mariage_certificate(TemplateView):
    template_name = "app/municipality/mayor/mariage_certificate.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['id']=self.kwargs['id']

        #RECUPERATION DES INFO DU USER CONNECTER
        context['person_id']=self.request.user.person_id
        user_connected=Person.objects.get(pk=context['person_id'])    
        context['profil']=user_connected 
        context['user']=self.request.user
        context["couple"] = Couple.objects.get(pk=context['id'])
        context["marriage"]= Marriage.objects.get(couple_id=context["couple"].pk)
        context["witness"]= Witness.objects.filter(marriage_id=context["marriage"].pk)
        print(context["witness"][0].person.firstname)
        return context
