from django.urls import path
from .views import *

# nom de l'application
app_name = 'BaseDonnee'

# liste des urls de l'application
urlpatterns = [
    path('', recherche, name='recherche'),
    path('suppression/<str:clef>', suppression, name='suppression'),
]