from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    expediteur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_envoyes')
    destinateur = models.ForeignKey(User, on_delete=models.CASCADE, related_name='messages_recus')
    contenu = models.TextField()
    date_envoi = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Message de {self.expediteur.username} à {self.destinateur.username}"
