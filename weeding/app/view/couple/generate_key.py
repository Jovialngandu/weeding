from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from app.models  import Couple
from app.models  import Request
from app.models  import Person
from django.utils import timezone
from django.urls import reverse

class generate_key(TemplateView):
    template_name ="app/couple/generate_key.html"
   
    def get_queryset(self):
            return  ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
       
        return context
    
    def post(self, request, *args, **kwargs):
      
        
        if request.POST['verify'] and request.POST['verify']!=request.POST['my_code']:
             verify=request.POST['verify']
             #^procedure de mise en couple
             partenaire_id=verify.split("-")[1]#personne id
             
             partenaire=Person.objects.get(pk=partenaire_id)
            #  new_request=Request
             couple=Couple.objects.create(person1_id=self.request.user.person_id,person2_id=partenaire_id)
             request=Request.objects.create(couple_id=couple.id,request_date=timezone.now().date()  ,request_status="En attente")
             request.save()

             
            
        return HttpResponseRedirect(reverse("dmMariage"))
    