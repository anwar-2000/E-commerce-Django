from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import View
from Catalogue.models import Produit 
from Paiements.models import Coupon


from decimal import Decimal

class Payment(View):
    def get(self,request,id):
        product_id =self.kwargs['id']
        id = product_id
        produit = Produit.objects.get(pk=id)
        if produit :
            context = {'produit_nom' : produit.nom,
                       'produit_photo': produit.photo.url,
                       'produit_quanitite' : produit.quantite,
                       'produit_prix' : produit.prix
                        }
            return render(request,'Paiements/index.html' ,context)
        else:
             return render(request,'Paiements/index.html')
    def post(self,request,id):
         quantite = request.POST.get('quantite')
         coupon = request.POST.get('coupon')
         produit = get_object_or_404(Produit, id=id)
         price = request.POST.get('price')
         url = reverse('checkout', args=[quantite, coupon, price])
         return HttpResponseRedirect(url)
        
class Card_Payment(View):
      def get(self, request, quantite, coupon, price):
        if coupon is not None:
             couponCodes = Coupon.objects.filter(code=coupon.replace(' ',''))
             if couponCodes.exists():
                 couponCode = couponCodes[0]
                 coupon_reduction = Decimal(str(couponCode.reduction))
                 price = (Decimal(price) * (100 - coupon_reduction)) / 100
                 message = f"le code est validé vous avez gagné une réduction de {coupon_reduction}%"
                 context = {
                          'price': price,
                        'quantite': quantite,
                         'message': message
                                          }
                 print(message , price)
                 return render(request, 'Paiements/gateway.html', context)
        else :
             message = "Vous pouvez bénéficier des coupons de réduction jusqu'à 80%, donc n'hésitez pas à nous visiter une autre fois, Merci"
             context = {
                          'price': price,
                        'quantite': quantite,
                         'message': message
                                          }
             return render(request, 'Paiements/gateway.html', context)



