from django.shortcuts import render
from django.http import HttpResponse

def inscription(request):
   
    return render(request, 'app/inscription.html')