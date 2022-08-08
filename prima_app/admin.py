from importlib.resources import path
from django.contrib import admin

from prima_app.models import Patient, RendezVous, Resultat

# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ['nom', 'prenom', 'genre', 'Age', 'groupe_sangin', 'date']
    search_fields = ['nom', 'prenom', 'genre', 'Age', 'groupe_sangin', 'date']
    list_filter = ['genre']
    list_per_page = 10


admin.site.register(Patient, PatientAdmin)


# enregistrement pour le les Rendevouz
class RendezVousAdmin(admin.ModelAdmin):
    list_display = ['nom_pat', 'nom_med', 'date_rv', 'description', 'status']
    search_fields = ['nom_med', 'date_rv']
    list_filter = ['status']
    list_per_page = 10


admin.site.register(RendezVous, RendezVousAdmin)


# enregistrement pour les Resultat
class ResultatAdmin(admin.ModelAdmin):
    list_display = ['num_res', 'nom_pat', 'nom_med', 'nom_serv', 'data_res', 'observation']
    search_fields = ['nom_patient', 'nom_serv']
    list_filter = ['nom_serv']
    list_per_page = 10


admin.site.register(Resultat, ResultatAdmin)