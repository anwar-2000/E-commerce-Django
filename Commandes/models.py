from django.db import models
from Utilisateurs.models import Utilisateur
from Catalogue.models import Produit

class EtatCommande(models.Model):
    nom = models.CharField(max_length=60)

class ArticleCommande(models.Model):
    produit = models.ForeignKey(Produit,on_delete=models.CASCADE)
    quantite = models.IntegerField()


class Commande(models.Model):
    utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    articles = models.ManyToManyField(ArticleCommande , related_name='produits')
    prix_totale = models.DecimalField(max_digits=5, decimal_places=2)
    paid = models.BooleanField(default=False)
    stripe_payment_id = models.CharField(max_length=150)
    addresse_du_livraison = models.TextField(max_length=150)
    mode_de_paiment = models.CharField(max_length=60)
    etat_de_commande = models.ForeignKey(EtatCommande,on_delete=models.CASCADE)