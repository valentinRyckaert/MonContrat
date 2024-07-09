from django.shortcuts import render

# fonctions d'affichage des pages html

def main(request):
    return render(request, 'main.html') # affichage de la page


def presentation(request):
    return render(request, 'presentation.html') # affichage de la page


def infos(request):
    return render(request, 'infos.html') # affichage de la page