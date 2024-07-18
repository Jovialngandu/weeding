from django.shortcuts import render
from django.http import HttpResponse
from app.models.Couple import Couple
from app.models.Marriage import Marriage
from app.models import Officer
from django.views.generic import TemplateView

class mariage_certificate(TemplateView):
    template_name = "app/municipality/mayor/mariage_certificate.html"
   
    def get_queryset(self):
            return ''
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # print(context)
        return context
def acte(request):
   
    return render(request, 'app/municipality/mayor/mariage_certificate.html')