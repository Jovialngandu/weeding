
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from app.models  import Person
from app.models  import Marriage
from app.models  import Request
from django.utils import timezone
from datetime import datetime, timedelta
from django.db.models import Count
from django.db.models.functions import ExtractMonth
from datetime import date


# class dashboard(TemplateView):
#     template_name = "app/municipality/dashboard.html"
   
#     def get_queryset(self):
#             return ''
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         # print(context)
#         return context

@method_decorator(login_required(login_url='/login'), name='dispatch') # sur `dispatch` : pour toutes les méthode HTTP(post, get, ...)
class index(TemplateView) :
    template_name = "app/municipality/dashboard.html"
    def  verify(self, **kwargs):
        context={}
        if self.request.user.is_staff:
            #RECUPERATION DES INFO DU USER CONNECTER
            context['person_id']=self.request.user.person_id
            self.template_name="app/municipality/dashboard.html"
            user_connected=Person.objects.get(pk=context['person_id'])    
            context['profil']=user_connected
            #RECUPERER LE NOMBRE DES MARIAGES CELEBRES
            celebrate_mariage_nbr=Marriage.objects.all().count
            context['nbr_celebrate']= celebrate_mariage_nbr



            #RECUPERER LE NOMBRE DES MARIAGES A VENIR ET LES MARIAGE A VENIR
            today = timezone.now().date()  # Obtient la date actuelle
            upcoming_mariages = Marriage.objects.filter(celebration_date__gte=today)
            context['nbr_upcoming_mariages']=upcoming_mariages.count()
            context['upcoming_mariages']=upcoming_mariages
            # print(upcoming_mariages[0].celebration_place)
            # print(upcoming_mariages.count())


            # DETERMINER LE NOMBRE DE MARIAGES CE MOI
            # Déterminer le premier et le dernier jour du mois actuel
            start_of_month = datetime(today.year, today.month, 1)
            # Pour obtenir le dernier jour du mois, on utilise le premier jour du mois suivant moins un jour
            next_month = start_of_month + timedelta(days=32)
            end_of_month = datetime(next_month.year, next_month.month, 1) - timedelta(days=1)

            # Filtrer les mariages qui ont lieu ce mois-ci
            mariages_this_month = Marriage.objects.filter(celebration_date__gte=start_of_month, celebration_date__lte=end_of_month)
            # print(mariages_this_month.count())
            context['mariages_this_month']=mariages_this_month.count()



            #RECUPERATION DU NOMBRE DES DOSSIER EN ATTENTE
            requests_attente_nbr=Request.objects.filter(request_status='En attente').count()
            context['request_attente_nbr']=requests_attente_nbr


            #RECUPERATION DU NOMBRE DES DOSSIER VALIDE
            requests_Valide_nbr=Request.objects.filter(request_status='Valide').count()
            context['request_Valide_nbr']=requests_Valide_nbr
        

            #RECUPERATION DU NOMBRE DES DOSSIER INVALIDE
            requests_invalide_nbr=Request.objects.filter(request_status='Non valide').count()
            context['request_invalide_nbr']=requests_invalide_nbr

            current_month = date.today().month
            marriages = Marriage.objects.filter(celebration_date__month__lte=current_month).annotate(month=ExtractMonth('celebration_date')).values('month').annotate(count=Count('id')).order_by('month')
            marriages_by_month = {marriage['month']: marriage['count'] for marriage in marriages}
            context['marriages_by_month']=marriages_by_month
            # print(marriages_by_month)
            return context
        else :
            self.template_name="app/couple/home.html"

            
            
    def get_context_data(self, **kwargs):
            datas = {}
            context = {**super().get_context_data(**kwargs), **datas}
            context=self.verify()
            return context
   
    def get(self, request, *args, **kwargs):
            return super().get(request, *args, **kwargs)
    def dispatch(self, *args, **kwargs):
            return super().dispatch(*args, **kwargs)