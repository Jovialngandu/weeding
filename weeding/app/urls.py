from django.urls import path
from app.view import connexion
from app.view import inscription
from app.view import code
from app.view import profil
from app.view import couples
from app.view import demandes
from app.view import   acte
from app.view import  infoCouple  
from app.view import historicMariage
from app.view import dashboard
from .view import auth_view, profile_view

from . import views

urlpatterns = [
    path("", dashboard.index.as_view(), name="dashboard"),
    # path("",dashboard.dashboard, name="dashboard"),
    path("login", auth_view.login.as_view(), name="login"),
    # path("login",connexion.connexion, name="connexion"),
    path("register", auth_view.register.as_view(), name="register"),
    # path("signin",inscription.inscription, name="inscription"),
    path("profil",profil.profil, name="profil"),
    path("couples",couples.couples, name="couples"),
    path("demandes",demandes.demandes, name="demandes"),
    path("acte",acte.acte, name="acte"),
    path("infoCouple",infoCouple.infoCouple, name="infoCouple"),
    path("historicMariage",historicMariage.historicMariage, name="historicMariage"),
    path("code",code.code, name="code"),
    
]