from django.forms import ModelForm
from .models import Form

# création du formulaire

class FormContrat(ModelForm):
    class Meta:
        model = Form # prend le modèle de la base de données
        fields = '__all__' # récupère l'ensemble des champs du modèle
