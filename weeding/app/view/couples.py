from django.shortcuts import render
from django.http import HttpResponse
from app.models.Couple import Couple
from app.models.Officer import Officer
def couples(request):
    context={'nbr':Couple.objects.all().count()}
    print(context)
    return render(request, 'app/couples.html',context)