from django.urls import path
from app.view import connexion
from app.view import inscription

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login",connexion.connexion, name="connexion"),
    path("signin",inscription.inscription, name="inscription"),
]