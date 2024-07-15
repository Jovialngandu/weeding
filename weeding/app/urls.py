from django.urls import path
from app.view import connexion
from app.view import inscription
from app.view import weeding
from app.view import profil
from app.view import couples
from app.view import demandes
from app.view import   acte
from app.view import  infoCouple  
from app.view import historicMariage
from app.view import dashboard

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login",connexion.connexion, name="connexion"),
    path("signin",inscription.inscription, name="inscription"),
    path("weeding",weeding.mariage, name="mariage"),
    path("profil",profil.profil, name="profil"),
    path("couples",couples.couples, name="couples"),
    path("demandes",demandes.demandes, name="demandes"),
    path("acte",acte.acte, name="acte"),
    path("infoCouple",infoCouple.infoCouple, name=" infoCouple"),
    path("historicMariage",historicMariage.historicMariage, name="historicMariage"),
    path("dashboard",dashboard.dashboard, name="dashboard"),
    
]