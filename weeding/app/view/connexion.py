from django.shortcuts import render
from django.http import HttpResponse

def connexion(request):
   
    return render(request, 'app/connexion.html')