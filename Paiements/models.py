from django.db import models
from ..Commandes.models import Commande

class Coupon(models.Model):
    code = models.CharField(max_length=15)
    reduction=models.DecimalField()
    date_de_expiration = models.DateTimeField()


class Transaction(models.Model):
    commande = models.ForeignKey(Commande)
    date = models.DateTimeField(auto_now=True)
    montant = models.DecimalField()