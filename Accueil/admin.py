from django.contrib import admin

# Register your models here.
from Utilisateurs.models import Utilisateur
from Catalogue.models import Produit
from Catalogue.models import Categorie


class ProduitAdmin(admin.ModelAdmin):
    list_filter = ("categorie",)
    list_display = ("nom", "quantite",)


admin.site.register(Utilisateur)
admin.site.register(Produit,ProduitAdmin)
admin.site.register(Categorie)