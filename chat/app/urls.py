from django.urls import path
from .views import *

urlpatterns = [
   path('', connexion, name='login'),
   path('deconnexion', deconnexion, name='deconnexion'),
   path('chat', chat, name='chat'),
   path('discussion/<int:id>', discussion, name='discussion')
]
