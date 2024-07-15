from django.shortcuts import render
from django.http import HttpResponse

def historicMariage(request):
   
    return render(request, 'app/historicMariage.html')