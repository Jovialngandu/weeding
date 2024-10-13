from django.shortcuts import render
from django.http import HttpResponse
from app.models.Couple import  Couple
from django.views.generic import TemplateView
from app.models  import Person
from app.models.User  import User
from app.models.Marriage  import Marriage
from django.http import HttpResponseRedirect
from django.urls import reverse
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
        context['couple']=Couple.objects.get(pk=kwargs['id'])
        context['couple_user1']=User.objects.filter(person_id=context['couple'].person1.id)
        context['couple_user2']=User.objects.filter(person_id=context['couple'].person2.id)      
        if  context['couple_user1'] :
             context['email_user1']=context['couple_user1'][0].email
        else:
             context['email_user1']="lambalia@gmail.com"
        if  context['couple_user2'] :
             context['email_user2']=context['couple_user2'][0].email
        else:
             context['email_user2']="lambalia@gmail.com"
             
    
        return context
    
    
class applicate_update(TemplateView):
     template_name = "app/municipality/update_couple.html"
   
     def get_queryset(self):
            return ''
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

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

        #  birthdate1=request.POST['partner1-birthdate']
        #  birthdate2=request.POST['partner2-birthdate']

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
         couple=Couple.objects.get(pk=self.kwargs['id'])
         #MODIFICATION PERSONNE1

         person1=Person.objects.get(pk=couple.person1.id)
         person1.firstname=firstname1
         person1.lastname=lastname1
         person1.middlename=middlename1
         person1.nationality=nationality1
         person1.phone_number=phone1
        #  person1.date_of_birth=birthdate1
         person1.place_of_birth=wherebirth1
         person1.sex=sex1
         person1.save()
         

         #MODIFICATION PERSONNE2

         person2=Person.objects.get(pk=couple.person2.id)
         person2.firstname=firstname2
         person2.lastname=lastname2
         person2.middlename=middlename2
         person2.nationality=nationality2
         person2.phone_number=phone2
        #  person2.date_of_birth=birthdate2
         person2.place_of_birth=wherebirth2
         person2.sex=sex2
         person2.save()
         marriage=Marriage.objects.filter(couple_id=couple.id)
         marriage[0].celebration_date=request.POST['marriage-date']
         marriage[0].save()
         print(marriage)
         

         return HttpResponseRedirect(reverse("update_couple", args=(self.kwargs['id'],)))
         