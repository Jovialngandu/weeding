from django.shortcuts import render
from django.http import HttpResponse

def code(request):
   
    return render(request, 'app/code.html')