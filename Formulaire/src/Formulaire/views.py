from django.shortcuts import render, redirect, get_object_or_404
from .forms import FormContrat
from .models import Form


# la page contrat récupère le formulaire pour l'afficher
def contrat(request):
    if request.method == 'POST':
        form = FormContrat(request.POST)
        if form.is_valid(): # si quelque chose a été saisi et que le tout est valide
            form.save() # enregistrement dans la base de données
            return redirect("Formulaire:validation", pk=form.cleaned_data['clef']) # redirection vers la page de validation
        context = {'form': form, 'erreur':True} # s'il n'est pas valide, on renvoie le formulaire avec une erreur
    else: # si rien n'a été encore saisi, on crée un formulaire vide
        form = FormContrat()
        context = {'form': form, 'erreur':False}
    return render(request, "contrat.html", context) # affichage de la page avec les données

# la page récupère un formulaire existant pour l'afficher
def existContrat(request, **clef):
    form = get_object_or_404(Form, pk=clef['pk']) # récupère le formualaire grâce à sa clef (erreur 404 si la clef est inconnue)
    if request.method == 'POST':
        form = FormContrat(request.POST, instance=form) # récupération des données de la base
        if form.is_valid(): # si quelque chose a été saisi et que le tout est valide
            form.save() # enregistrement dans la base de données
            return redirect("Formulaire:validation", pk=form.cleaned_data['clef']) # redirection vers la page de validation
        context = {'form': form, 'erreur':True} # s'il n'est pas valide, on renvoie le formulaire avec une erreur
    else: # si rien n'a été encore saisi, on crée un formulaire vide (à priori inutilisé, ce else est présent en cas de problème)
        form = FormContrat(instance=form)
        context = {'form': form, 'erreur':False}
    return render(request, "contrat.html", context) # affichage de la page avec les données

# la page récupère les données du formulaire et les affiche
def validation(request, **clef):
    form = get_object_or_404(Form, pk=clef['pk']) # récupère le formualaire grâce à sa clef (erreur 404 si la clef est inconnue)
    liste_partenaires = form.partenaires.split("\n") # récupérations des partenaires
    copies = len(liste_partenaires) # calcul du nombre de copies en fonction du nombre de partenaires
    liste_contribution = form.partenaires.split("\n") # récupérations des différentes contributions
    context = { # récupérations des données pour les afficher sur la page
        'Form': form,
        'liste_partenaires': liste_partenaires,
        'liste_contribution': liste_contribution,
        'copies': copies
    } 
    return render(request, 'validation.html', context) # affichage de la page avec les données
