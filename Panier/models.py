from django.db import models
from Utilisateurs.models import Utilisateur
from  Catalogue.models import Produit


class Panier(models.Model):
    utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)

class ArticlePanier(models.Model):
    produit = models.ForeignKey(Produit,on_delete=models.CASCADE)
    quanitite = models.IntegerField()
    panier = models.ForeignKey(Panier,on_delete=models.CASCADE)
    

