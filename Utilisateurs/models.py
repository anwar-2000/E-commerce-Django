from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager

class Utilisateur(AbstractUser):
    username = None
    email = models.EmailField(unique=True)
    mobile = models.CharField(max_length=14,default="")
    is_verified = models.BooleanField(default=False)
    email_token=models.CharField(max_length=100,null=True,blank=True)
    forgot_password = models.CharField(max_length=100,null=True,blank=True)
    addresse_de_livraison = models.TextField(max_length=150)

    objects = UserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class ProfilUtilisateur(models.Model):
    utilisateur = models.OneToOneField(Utilisateur,on_delete=models.CASCADE)
    photo_profile = models.ImageField(upload_to='images-profiles')
    bio=models.TextField(max_length=100)

class SessionUtilisateur(models.Model):
    utilisateur = models.ForeignKey(Utilisateur,on_delete=models.CASCADE)
    jeton_acces = models.CharField(max_length=100)
    date_expiration = models.DateTimeField(auto_now_add=True)
