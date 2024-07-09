import secrets
import string
from django.db import models
from django import forms

# création de la clef d'identification
def clef_create():
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(25))
    return password

# création du modèle de données pour la BDD
class Form(models.Model):
    date_signature = models.DateField()
    lieu_signature = models.CharField(max_length=32)
    nom_exerce = models.CharField(max_length=32)
    partenaires = models.TextField()
    activites = models.TextField()
    adresse = models.CharField(max_length=32)
    code_postal = models.IntegerField()
    ville = models.CharField(max_length=32)
    date_debut = models.DateField()
    contribution = models.TextField()
    partage_profit = models.TextField()
    pourcentage_cheques = models.IntegerField()
    temps_retrait = models.CharField(max_length=32)
    etat_lois = models.CharField(max_length=32)
    avocat = models.CharField(max_length=32)
    clef = models.CharField(primary_key=True, default=clef_create(), max_length=32)