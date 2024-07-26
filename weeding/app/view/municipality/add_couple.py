from django.shortcuts import render
from django.http import HttpResponse
from app.models.Couple import  Couple
from django.views.generic import TemplateView
from app.models  import Person
from app.models  import Request
from app.models  import User
from django.utils import timezone
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

@method_decorator(login_required(login_url='/login'), name='dispatch') # sur `dispatch` : pour toutes les méthode HTTP(post, get, ...)
class add_couple(TemplateView):
    template_name = "app/municipality/add_couple.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)


        #RECUPERATION DES INFO DU USER CONNECTER
        context['person_id']=self.request.user.person_id
        user_connected=Person.objects.get(pk=context['person_id'])    
        context['profil']=user_connected
    
        return context
    def post(self, request, *args, **kwargs):
         #firstname
         firstname1=request.POST['partner1-firstname']  
         firstname2=request.POST['partner2-firstname']

         #lastname
         lastname1=request.POST['partner1-lastname']
         lastname2=request.POST['partner2-lastname']
        
         #middlename

         middlename1=request.POST['partner1-middlename']
         middlename2=request.POST['partner2-middlename']
         
         
         #birthdate

         birthdate1=request.POST['partner1-birthdate']
         birthdate2=request.POST['partner2-birthdate']

         #partner1-wherebirth
         wherebirth1=request.POST['partner1-wherebirth']
         wherebirth2=request.POST['partner2-wherebirth']

        #SEX
         sex1=request.POST['sex1']
         sex2=request.POST['sex2']

         #nationality
         nationality1=request.POST['partner1-nationality']
         nationality2=request.POST['partner2-nationality']

         #EMAIL
         email1=request.POST['email1']
         email2=request.POST['email2']

         #PHONE
         phone1=request.POST['phone1']
         phone2=request.POST['phone2']
         person1 = Person(lastname=lastname1,
                           firstname=firstname1,
                             middlename=middlename1,
                               nationality=nationality1,
                                 phone_number=phone1, 
                                 sex=sex1,
                                 date_of_birth= birthdate1
                                 ,place_of_birth=wherebirth1)
	      
         person1.save()
         person2 = Person(lastname=lastname2,
                              firstname=firstname2,
                                middlename=middlename2,
                                  nationality=nationality2,
                                    phone_number=phone2, 
                                    sex=sex2,
                                    date_of_birth= birthdate2
                                    ,place_of_birth=wherebirth2)
            
         person2.save()
         user1 = User.objects.create_user(email= email1, password="wedding", person=person1)
         user1.save()
         user2 = User.objects.create_user(email= email2, password="wedding", person=person2)
         user2.save()
         couple=Couple.objects.create(person1_id=person1.id,person2_id=person2.id)
        
         couple.save()
         request=Request.objects.create(couple_id=couple.id,request_date=timezone.now().date()  ,request_status="En attente")
         request.save()
          
          

         return HttpResponseRedirect(reverse("add_couple"))
