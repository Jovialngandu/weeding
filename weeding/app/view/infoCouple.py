from django.shortcuts import render
from django.http import HttpResponse
from app.models.Couple import Couple
def  infoCouple(request):
   
    return render(request, 'app/infoCouple.html')