from django.shortcuts import render
from django.http import HttpResponse
from app.models.Couple import Couple
from app.models.Couple import Person
from app.models.Marriage import Marriage
from app.models.Request import Request
from app.models.Witness import Witness
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse

class couple_details(TemplateView):
    template_name = "app/municipality/couple_details.html"
   
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
        try:
             context["marriage"]= Marriage.objects.get(couple_id=context["couple"].pk)
             context["witness"]= Witness.objects.filter(marriage_id=context["marriage"].pk)
             context["status"]=str(Request.objects.filter(couple_id=context["couple"].pk)[:1][0].request_status)
        
        
             if context["status"]=="Valide":
                        context["valide"]=1
             elif  context["status"]=="En attente":
                context["en_attente"]=1
             else:
                context["non_valide"]=1
              
        except Exception  as e:
                  print(e)
        return context
    
class couple_detail_update_status(couple_details):

            template_name = "app/municipality/couple_details.html"
            
            def post(self, request, *args, **kwargs):
                 demande=Request.objects.filter(couple_id=self.kwargs['id'])[:1][0]
                 demande.request_status=request.POST["list-radio"]
                 demande.save()
                
                 return HttpResponseRedirect(reverse("infoCouple" ,args=(self.kwargs['id'],)))


     