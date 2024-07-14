from django.shortcuts import render
from django.http import HttpResponse

def  infoCouple(request):
   
    return render(request, 'app/infoCouple.html')