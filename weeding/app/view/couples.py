from django.shortcuts import render
from django.http import HttpResponse

def couples(request):
   
    return render(request, 'app/couples.html')