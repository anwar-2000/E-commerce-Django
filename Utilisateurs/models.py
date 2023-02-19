from django.db import models

class Utilisateur(models.Model):
    email = models.EmailField()
    username = models.CharField(max_length=50)
    addresse_de_livraison = models.TextField(max_length=150)
    mot_de_passe = models.CharField(max_length=50)

class ProfilUtilisateur(models.Model):
    utilisateur = models.OneToOneField(Utilisateur)
    photo_profile = models.ImageField(upload_to='images-profiles')
    bio=models.TextField(max_length=100)

class SessionUtilisateur(models.Model):
    utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    jeton_acces = models.CharField(max_length=100)
    date_expiration = models.DateTimeField(auto_now_add=True)
