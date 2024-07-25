from django.http import HttpResponse
from app.models  import Person
from app.models  import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
@method_decorator(login_required(login_url='/login'), name='dispatch') # sur `dispatch` : pour toutes les méthode HTTP(post, get, ...)

class profil(TemplateView):
    template_name = "app/public/profil.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #RECUPERATION DES INFO DU USER CONNECTER
        context['person_id']=self.request.user.person_id
        user_connected=Person.objects.get(pk=context['person_id'])    
        context['profil']=user_connected 
        context['email']=self.request.user.email
        context['role']=self.request.user.is_staff
       
        return context
class update_profil(TemplateView):
     template_name="app/public/profil"
     def get_queryset(self):
            return ''
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context
     def post(self, request, *args, **kwargs):
            fullname=request.POST.get("fullname")
            fullname=fullname.split('--')
            firstname=fullname[0].strip()
            lastname=fullname[1].strip()
            middlename=fullname[2].strip()
            email=request.POST.get("email")
            phone=request.POST.get("phone")
            user=User.objects.get(pk=self.request.user.id) 
            person=Person.objects.get(pk=self.request.user.person_id)
            person.firstname=firstname
            person.lastname=lastname
            person.middlename=middlename
            person.phone_number=phone
            person.save()
            user.email=email
            user.save()
            
            return HttpResponseRedirect(reverse("profil"))
           

      