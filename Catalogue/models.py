from django.db import models

from  Utilisateurs.models import Utilisateur 

class Categorie(models.Model):
    nom = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nom}"


class Produit(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField(max_length=1500)
    photo = models.ImageField(upload_to='photos-produits')
    quantite = models.IntegerField()
    prix = models.DecimalField(max_digits=5, decimal_places=2)
    categorie = models.ManyToManyField(Categorie)

    def __str__(self):
        return f"{self.nom} ({self.quantite})"


class Commentaire(models.Model):
    auteur = models.ForeignKey(Utilisateur , on_delete=models.PROTECT)
    produit = models.ForeignKey(Produit,on_delete=models.CASCADE)
    contenu = models.TextField(max_length=750)

    def __str__(self):
        return f"{self.auteur}"
