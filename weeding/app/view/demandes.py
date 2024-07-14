from django.shortcuts import render
from django.http import HttpResponse

def demandes(request):
   
    return render(request, 'app/demandes.html')