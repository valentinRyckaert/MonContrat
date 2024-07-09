installation de git :
    allez à l'adresse https://git-scm.com/download/win
    cliquez sur '64-bit Git for Windows Setup'
    ouvrez le .exe téléchargé
    suivez les instructions d'installation (les paramettres séléctionner par défauts fonctionnent, vous pouvez spamer le bouton next)


Accès au projet django

Ouvrir git bash et executer les commandes suivantes :

    python
    [téléchargez python depuis microsoft store]
    pip install --upgrade pip
    git clone [le code https gitlab du projet]
    [entrez vos identifiants]
    cd formulaire-django
    cd Formulaire
    source .env/bin/activate
    pip install -r requirements.txt
    cd src
    python manage.py runserver


Dans le message qui s'affiche, une url s'affiche : c'est celle du localhost qu'utilise django. Copier cette url et coller la sur la barre de recherche de votre navigateur (vous pouvez aussi simplement cliquer dessus).

Pour arrêter le serveur, faîtes Ctrl+C dans le terminal.

Les fichiers __init__, les dossiers migrations et __pycache__ ne sont pas à supprimer. Ils servent à faire fonctionner correctement la hérarchie de dossier django.