from django.shortcuts import render
from django.http import HttpResponse

def profil(request):
   
    return render(request, 'app/profil.html')