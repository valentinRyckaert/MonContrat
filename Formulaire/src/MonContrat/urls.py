from django.contrib import admin
from django.urls import path, include
from .views import *

# liste des urls de l'application principale
urlpatterns = [
    path('', main, name='main'),
    path('infos/', infos, name='infos'),
    path('presentation/', presentation, name='presentation'),
    path('contrat/', include('Formulaire.urls')),
    path('recherche/', include('BaseDonnee.urls')),
    path('djformadmini/', admin.site.urls),
]