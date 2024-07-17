from django.shortcuts import render
from django.http import HttpResponse
from app.models import  Person
from app.models import  Admin
from app.models import  Mayor  

def demandes(request):
   
    return render(request, 'app/demandes.html')