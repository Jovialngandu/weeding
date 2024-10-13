from django.shortcuts import render
from django.http import HttpResponse
from app.models  import Person
from app.models  import Marriage
from app.models  import Mayor
from app.models  import Witness
from app.models  import Couple
from app.models  import User
from app.models  import Request
from django.views.generic import TemplateView

class dmMariage(TemplateView):
    
    template_name ="app/couple/dmMariage.html"
   
    def get_queryset(self):
            return  " "
    def is_in_couple(self):
         is_in=False
         if Couple.objects.filter(person1_id=self.request.user.person_id).exists() or    Couple.objects.filter(person2_id=self.request.user.person_id).exists() :
                is_in=True

         return  is_in
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)    
        #RECUPERATION DES INFO DU USER CONNECTER
        context['person_id']=self.request.user.person_id
        self.template_name="app/couple/dmMariage.html"
        user_connected=Person.objects.get(pk=context['person_id']) 
        context["code"] = self.generate()   
        context['profil']=user_connected
        if self.is_in_couple():
           try:
              if Couple.objects.filter(person1_id=self.request.user.person_id).exists():
                    context['partenaire']= Couple.objects.filter(person1_id=self.request.user.person_id)[0].person1
                    context["couple"] = Couple.objects.filter(person1_id=self.request.user.person_id)[0]
                    context['marriage']=Marriage.objects.filter(couple_id=context["couple"].id)[0]
              else:
                    context['partenaire']= Couple.objects.filter(person2_id=self.request.user.person_id)[0].person2
                    context["couple"] = Couple.objects.filter(person2_id=self.request.user.person_id)[0]
                    context['marriage']=Marriage.objects.filter(couple_id=context["couple"].id)[0]

           except Exception  as e:
                  print(e)
        
        

                
            #   if Marriage.objects.filter(person1_id=self.request.user.person_id).exists():

            #        context["marriage"]= Marriage.objects.get(couple_id=context["couple"].pk)
            #        context["witness"]= Witness.objects.filter(marriage_id=context["marriage"].pk)
            #        context["status"]=str(Request.objects.filter(couple_id=context["couple"].pk)[:1][0].request_status)

            #   else:
            #        context["marriage"]= Marriage.objects.get(couple_id=context["couple"].pk)
            #        context["witness"]= Witness.objects.filter(marriage_id=context["marriage"].pk)
            #        context["status"]=str(Request.objects.filter(couple_id=context["couple"].pk)[:1][0].request_status)
                    
                       
        print( self.is_in_couple())
        return context
    
    def generate(self):
         key= str(self.request.user.id)+"dmAzjnjzclxqsakecccc-"+str(self.request.user.person_id)
         return key