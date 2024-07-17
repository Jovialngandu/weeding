from django.shortcuts import render
from django.http import HttpResponse
from app.models.User import User
def inscription(request):
   
    return render(request, 'app/inscription.html')