from django.shortcuts import render
from django.http import HttpResponse
from app.models.Couple import Couple
from app.models.Marriage import Marriage
from app.models import Officer

def acte(request):
   
    return render(request, 'app/acte.html')