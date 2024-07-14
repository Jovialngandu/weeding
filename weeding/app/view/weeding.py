from django.shortcuts import render
from django.http import HttpResponse

def mariage(request):
   
    return render(request, 'app/mariage.html')