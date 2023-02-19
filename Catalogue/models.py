from django.db import models



class Categorie(models.Model):
    nom = models.CharField(max_length=100)


class Produit(models.Model):
    nom = models.CharField(max_length=150)
    description = models.TextField(max_length=1500)
    photo = models.ImageField(upload_to='photos-produits')
    quantite = models.IntegerField()
    prix = models.DecimalField()
    categorie = models.ManyToManyField(Categorie)


class Commentaire(models.Model):
    #auteur = models.ForeignKey(Utilisateur)
    produit = models.ForeignKey(Produit)
    contenu = models.TextField(max_length=750)
