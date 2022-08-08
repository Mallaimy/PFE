
from django.db import models
from django.utils import timezone

# Create your models here.

# choicefiled for gender
Choise = [
    ("M", "Masculin"),
    ("F", "Feminin"),
    ]
# choice for group sangin

ChoiseRHS = [
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-"),
    ]

# choice for services
Choiceserv = [
        ('Echo abdominal', 'Echo abdominal'),
        ('Echo Pelvienne', 'Echo Pelvienne'),
        ('Echo Arbre urinaire', 'Echo Arbre urinaire'),
        ('Echo Obstétricale', 'Echo Obstétricale'),
        ('Echo Obstétrical 3D/4D', 'Echo Obstétrical 3D/4D'),
        ('Echo mamaire(sein)', 'Echo mamaire(sein)'),
        ('Echo parties moles', 'Echo parties moles'),
        ('Echo bourses(Testicules)', 'Echo bourses (Testicules)'),
        ('Echo épaule-Genoux', 'Echo épaule-Génoux'),
        ('Echo Doppler', 'Echo Doppler'),
        ('TSA','TSA'),
        ('Membre inférieur', 'Membre inférieur'),
        ('Membres inférieur', 'Membres inférieur'),
        ('Bourses', 'Bourses'),
]

#_____________________Creation de la base de données par le ORM de Django_____________________________________________

# la table patient

class Patient(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    genre = models.CharField(max_length=5, choices=Choise)
    Age = models.IntegerField()
    groupe_sangin = models.CharField(max_length=5, choices=ChoiseRHS)
    date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nom

    class Meta:
        ordering = ['date']
# la table Medecin

class Medecin(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    genre = models.CharField(max_length=5, choices=Choise)
    specialite = models.CharField(max_length=50)
    telephone = models.IntegerField()

    def __str__(self):
        return self.nom

# la table Service

class Service(models.Model):
    nom = models.CharField(max_length=50, choices=Choiceserv)
    prix = models.DecimalField( max_digits=10, decimal_places=3)
    data_srv = models.DateField(default=timezone.now)

    def __str__(self):
        return self.nom
# la table Resultat

class Resultat(models.Model):
    num_res = models.CharField(max_length=10)
    nom_pat = models.ForeignKey(Patient, on_delete=models.CASCADE)
    nom_med = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    nom_serv = models.ForeignKey(Service, on_delete=models.CASCADE)
    data_res = models.DateField(default=timezone.now)
    observation = models.TextField()

    def __str__(self):
        return str(self.nom_pat)
# la table Rendez_vous

class RendezVous(models.Model):
    nom_pat =models.ForeignKey(Patient, on_delete=models.CASCADE)
    nom_med = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    date_rv = models.DateTimeField()
    description = models.TextField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return str(self.nom_pat)

