from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from app.models  import Person
from app.models  import User
from django.http import HttpResponseRedirect
from django.urls import reverse

class create_officer(TemplateView):
    template_name = "app/municipality/mayor/create_officer.html"
   
    def get_queryset(self):
            
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        print("hello")
        # print(context)
        return context
    
    def post(self, request, *args, **kwargs):
         
         #firstname
         firstname1=request.POST['firstname']  
         #lastname
         lastname1=request.POST['lastname']       
         #middlename
         middlename1=request.POST['middlename']       
         #birthdate
         birthdate1=request.POST['date_of_birth']
         #partner1-wherebirth
         wherebirth1=request.POST['place_of_birth']
        #SEX
         sex1=request.POST['sex']
         #nationality
         nationality1=request.POST['nationality']       
         #EMAIL
         email1=request.POST['email']      
         #PHONE
         phone1=request.POST['phone_number']   
         password=request.POST['password']  
         confirmpasword=request.POST['confirm_password']  
         print(request.POST)   
         if  password==confirmpasword:
            person1 = Person(lastname=lastname1,
                            firstname=firstname1,
                                middlename=middlename1,
                                nationality=nationality1,
                                    phone_number=phone1, 
                                    sex=sex1,
                                    date_of_birth= birthdate1
                                    ,place_of_birth=wherebirth1)
            
            person1.save()        
            user1 = User.objects.create_user(email= email1, password= password, person=person1,is_staff=True)
            user1.save()
         
         return   HttpResponseRedirect(reverse("test"))
