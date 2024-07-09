from django.shortcuts import render, get_object_or_404, redirect
from Formulaire.models import Form
from .forms import RechercheContrat


# la page contrat récupère le formulaire pour l'afficher
def recherche(request):
    if request.method == 'POST':
        saisie = RechercheContrat(request.POST)
        if saisie.is_valid(): # si quelque chose a été saisi et que le tout est valide
            # recherche de la clef correspondant au formulaire
            for occur in Form.objects.raw("SELECT clef FROM Formulaire_form"):
                if saisie.cleaned_data['clef'] == occur.clef:
                    return redirect("Formulaire:validation", pk=saisie.cleaned_data['clef'])
            # si rien n'a été trouvé, on affiche une erreur
            return render(request, "recherche.html", {'form': saisie, 'exist': False})
    else:
        saisie = RechercheContrat()
    return render(request, "recherche.html", {'form': saisie, 'exist': True})


def suppression(request, clef):
    form = get_object_or_404(Form, pk=clef) # récupération du formulaire par la clef
    form.delete() # suppression
    return render(request, 'suppression.html')
