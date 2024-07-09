from django import forms

# formulaire pour récupérer la clef d'identification
class RechercheContrat(forms.Form):
    clef = forms.CharField(max_length=25)
