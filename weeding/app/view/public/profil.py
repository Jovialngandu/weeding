from django.http import HttpResponse
from app.models import  Admin 
from app.models.Witness import  Witness
from app.models  import Person
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
        print(context)
        return context
        # 
      