from django.shortcuts import render
from django.views.generic import ListView , DetailView 
from .models import Produit , Categorie

class AllProduct(ListView):
    template_name='Catalogue/index.html'
    model = Produit
    context_object_name = "produits"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        return context
   

class ProductByCategory(ListView):
    model = Produit
    template_name= "Catalogue/category.html"
    context_object_name = "produits"

    def get_queryset(self) :
        queryset = super().get_queryset()
        categorie = self.kwargs.get('category')
        queryset2 = Categorie.objects.get(nom=categorie)
        if categorie and queryset2 :
            queryset = queryset.filter(categorie = queryset2)
            return queryset
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Categorie.objects.all()
        context['current_category'] = self.kwargs.get('category', '')
        return context


class Productdetail(DetailView):
    model = Produit
    template_name= "Catalogue/detail.html"
    context_object_name = 'produit'