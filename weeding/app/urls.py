from django.urls import path
from app.view.public import couple_login
from app.view.couple import signin
from app.view.couple import home
from app.view.couple import dmMariage
from app.view.couple import verification
from app.view.couple import generate_key
from app.view.municipality.mayor import create_officer
from app.view.public import profil
from app.view.municipality import all_couple
from app.view.municipality import all_demand
from app.view.municipality.mayor import   mariage_certificate
from app.view.municipality import  couple_details  
from app.view.municipality import historic_mariage
from app.view.municipality import add_couple
from app.view.municipality import update_couple
 
# from app.view.municipality import dashboard
from app.view.municipality import dashboard
from .view.public import profile_view
from .view.public import auth_view

from .view import test
from . import views

urlpatterns = [

    #couple
              path("generate_key",generate_key.generate_key.as_view(), name="generate_key"),  
              path("signin_couple",signin.signin.as_view(), name="signin_couple"),  
              path("couple_login",couple_login.connexion.as_view(), name="couple_login"),
              path("home",home.home.as_view(), name="home"),
              path("dmMariage",dmMariage.dmMariage.as_view(), name="dmMariage"),
              path("verification",verification.verification.as_view(), name="verification"),
    #municipality
              path("",dashboard.index.as_view(), name="dashboard"),
              path("couples",all_couple.couples.as_view(), name="couples"),
              path("demandes",all_demand.all_demand.as_view(), name="demandes"),
              path("historicMariage",historic_mariage.historic_mariage.as_view(), name="historicMariage"),
              path("add_couple",add_couple.add_couple.as_view(), name="add_couple"),

              path("infoCouple/<int:id>",couple_details.couple_details.as_view(), name="infoCouple"),
              path("infoCouple_update/<int:id>",couple_details.couple_detail_update.as_view(), name="infoCouple_update"), 
              path("update_couple/<int:id>",update_couple.update_couple.as_view(), name="update_couple"),
              path("update_couple_applicate/<int:id>",update_couple.applicate_update.as_view(), name="update_couple_applicate"),


    #municipality/mayor
              path("create_user",create_officer.create_officer.as_view(), name="create_user"),
              path("acte/<int:id>",mariage_certificate.mariage_certificate.as_view(), name="acte"),
              
    #public
             path("logout", auth_view.logout.as_view(), name="logout"),
             path("login", auth_view.login.as_view(), name="login"),
           
             path("register", auth_view.register.as_view(), name="register"),
             # path("signin",inscription.inscription, name="inscription"),
             path("profil",profil.profil.as_view(), name="profil"),
             path("update_profil",profil.update_profil.as_view(), name="update_profil"),
    #admin  


    #test  
             path("test",test.testView.as_view(), name="test"),

    

]