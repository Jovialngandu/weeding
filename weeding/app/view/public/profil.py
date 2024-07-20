from django.http import HttpResponse
from app.models import  Admin 
from app.models.Witness import  Witness
from django.views.generic import TemplateView

class profil(TemplateView):
    template_name = "app/public/profil.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
      