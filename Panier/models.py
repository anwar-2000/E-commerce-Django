from django.db import models
from..Utilisateurs.models import Utilisateur
from ..Catalogue.models import Produit


class Panier(models.Model):
    utilisateur = models.ForeignKey(Utilisateur)

class ArticlePanier(models.Model):
    produit = models.ForeignKey(Produit)
    quanitite = models.IntegerField()
    panier = models.ForeignKey(Panier)
    

