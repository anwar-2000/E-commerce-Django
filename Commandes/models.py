from django.db import models
from ..Utilisateurs.models import Utilisateur


class EtatCommande(models.Model):
    nom = models.CharField(max_length=60)

class ArticleCommande(models.Model):
    produit = models.ForeignKey()
    quantite = models.IntegerField()


class Commande(models.Model):
    utilisateur = models.ForeignKey(Utilisateur)
    articles = models.ManyToManyField(ArticleCommande)
    prix_totale = models.DecimalField()
    addresse_du_livraison = models.TextField(max_length=150)
    mode_de_paiment = models.CharField(max_length=60)
    etat_de_commande = models.ForeignKey(EtatCommande)