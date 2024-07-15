from django.shortcuts import render
from django.http import HttpResponse

def acte(request):
   
    return render(request, 'app/acte.html')