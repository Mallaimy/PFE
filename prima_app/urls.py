from django.urls import path
from .views import  Acceuil, CreatePatient, CreateRendezVous, CreateResultat, DeletePatient, DeleteRendezVous, DeleteResultat,Home, AdminLoginView, ListPatient, ListRendezVous, ListResultat, UpdatePatient, UpdateRendezVous, UpdateResultat
from django.contrib.auth.views import LogoutView

urlpatterns = [

    path('login/', AdminLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('', Acceuil.as_view(), name='acceuil'),
    path('home/', Home.as_view(), name="home"),




    path('patients/', ListPatient.as_view(), name="patient-list"),
    path('create/', CreatePatient.as_view(), name='patient-create'),
    path('update/<int:pk>/', UpdatePatient.as_view(), name='patient-update'),
    path('delete/<int:pk>/', DeletePatient.as_view(), name='patient-delete'),


# les urls pour les rendez_vous
    path('rendezvous/', ListRendezVous.as_view(), name="rv-list"),
    path('create-rv/', CreateRendezVous.as_view(), name='rv-create'),
    path('updateRv/<int:pk>/', UpdateRendezVous.as_view(), name='rv-update'),
    path('deleteRv/<int:pk>/', DeleteRendezVous.as_view(), name='rv-delete'),


# les urls pour le resultats

    path('resultat/', ListResultat.as_view(), name='resultat-list'),
    path('createRes/', CreateResultat.as_view(), name='resultat-create'),
    path('updateRes/<int:pk>/', UpdateResultat.as_view(), name='resultat-update'),
    path('deleteRes/<int:pk>/', DeleteResultat.as_view(), name='resultat-delete'),
]