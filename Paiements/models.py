from django.db import models
from Commandes.models import Commande

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    reduction=models.DecimalField(max_digits=5, decimal_places=2)
    date_de_expiration = models.DateTimeField()


class Transaction(models.Model):
    commande = models.ForeignKey(Commande,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    montant = models.DecimalField(max_digits=5, decimal_places=2)