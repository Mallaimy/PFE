from django.shortcuts import render
from prima_app.models import Patient, RendezVous, Resultat
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.



class AdminLoginView(LoginView):
    template_name = 'prima_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('home')


class Home(LoginRequiredMixin, TemplateView):
    template_name = "prima_app/home.html"


class Acceuil(TemplateView):
    template_name = "prima_app/acceuil.html"


# _____________________________BACKEND_________________________________|


class ListPatient(ListView):
    model = Patient
    queryset = Patient.objects.all()



class CreatePatient(CreateView):
    model = Patient
    fields = "__all__"
    success_url = reverse_lazy("patient-list")


class UpdatePatient(UpdateView):
    model = Patient
    fields = "__all__"
    success_url = reverse_lazy("patient-list")

class DeletePatient(DeleteView):
    queryset = Patient.objects.all()
    success_url = reverse_lazy("patient-list")

#_________________ Rendez_vous_________________________________________|

class ListRendezVous(ListView):
    model = RendezVous
    queryset = RendezVous.objects.all()


class CreateRendezVous(CreateView):
    model = RendezVous
    fields = "__all__"
    success_url = reverse_lazy("rv-list")

class UpdateRendezVous(UpdateView):
    model = RendezVous
    fields = "__all__"
    success_url = reverse_lazy("rv-list")

class DeleteRendezVous(DeleteView):
    queryset = RendezVous.objects.all()
    success_url = reverse_lazy("rv-list")

#_________________ Resultat_________________________________________


class ListResultat(ListView):
    model = Resultat
    queryset = Resultat.objects.all()


class CreateResultat(CreateView):
    model = Resultat
    fields = "__all__"
    success_url = reverse_lazy("resultat-list")

class UpdateResultat(UpdateView):
    model = Resultat
    fields = "__all__"
    success_url = reverse_lazy("resultat-list")

class DeleteResultat(DeleteView):
    queryset = Resultat.objects.all()
    success_url = reverse_lazy("resultat-list")