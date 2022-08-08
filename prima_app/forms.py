from dataclasses import field
from django import forms
from prima_app import models
from prima_app.models import Patient


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = "__all__"

        