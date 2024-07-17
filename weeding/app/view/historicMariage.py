from django.shortcuts import render
from django.http import HttpResponse
from app.models import  Admin 
from app.models.Witness import  Witness


def historicMariage(request):
   
    return render(request, 'app/historicMariage.html')