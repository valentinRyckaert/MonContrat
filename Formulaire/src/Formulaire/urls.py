from django.urls import path, include
from .views import *

# nom de l'application pour les urls
app_name = 'Formulaire'

# liste des urls de l'application 'Formulaire'
urlpatterns = [
    path('', contrat, name='contrat'),
    path('<str:pk>', existContrat, name='existContrat'),
    path('validation/<str:pk>', validation, name='validation'),
]
