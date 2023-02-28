from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render , redirect
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.urls import reverse 
from django.contrib import messages
from django.views import View
from Catalogue.models import Produit 
from Paiements.models import Coupon
from django.conf import settings
from Commandes.models import Commande
from Utilisateurs.models import Utilisateur
LOGIN_URL = reverse_lazy('loginPage')
"""
  STRIPE
"""
import stripe
"""

"""

stripe.api_key = settings.STRIPE_API_KEY



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
         product_id =self.kwargs['id']
         id=product_id
         produit = get_object_or_404(Produit, pk=id)
         price = request.POST.get('price')
         url = reverse('checkout', args=[quantite, coupon, price,id])
         return HttpResponseRedirect(url)
    
@method_decorator(login_required(login_url=LOGIN_URL), name='dispatch')
class Card_Payment(View):
      def get(self, request, quantite, coupon, price,id):
        if coupon is not None:
             couponCodes = Coupon.objects.filter(code=coupon.replace(' ',''))
             if couponCodes.exists():
                 couponCode = couponCodes[0]
                 coupon_reduction = Decimal(str(couponCode.reduction))
                 price = (Decimal(price) * (100 - coupon_reduction)) / 100
                 message = f"le code est validé vous avez gagné une réduction de {coupon_reduction}%"
                  # Create Stripe payment intent
                 intent = stripe.PaymentIntent.create(
                 amount=int(price *100),
                 currency="eur",
                 metadata={
                "price": price,
                "coupon": coupon,
        },
                                                    )
                 context = {
                          'client_secret': intent.client_secret,
                          'price': price,
                          'quantite': quantite,
                          'message': message
                                          }
                 return render(request, 'Paiements/gateway.html', context)
             else :
                 message = "Vous pouvez bénéficier des coupons de réduction jusqu'à 80%, donc n'hésitez pas à nous visiter une autre fois, Merci"
                 context = {
                          'price': price,
                        'quantite': quantite,
                         'message': message
                                          }
                 return render(request, 'Paiements/gateway.html', context)



@login_required
def payment_process(request):
    # Retrieve the payment intent client secret and order information from the form data
    client_secret = request.POST['client_secret']
    user_id = request.user.id()
    product_id= request.POST['produit_id']
    price= request.POST['price']
    user = Utilisateur.objects.get(pk=user_id)
    order = Commande.objects.create(utilisateur=user_id,articles=product_id,prix_totale=price,addresse_du_livraison=user.addresse_de_livraison)

    try:
        # Confirm the payment with Stripe
        intent = stripe.PaymentIntent.confirm(client_secret)

        # Update the order status to "paid"
        order.paid = True
        order.stripe_payment_id = intent.id
        order.save()


        # Display a success message to the user
        messages.success(request, 'Thank you for your purchase!')

        # Redirect the user to a success page
        #return redirect('payment_success')
    except stripe.error.CardError as e:
        # Display an error message to the user
        messages.error(request, 'There was an error processing your payment: {}'.format(e))

        # Redirect the user to the payment form page
        #return redirect('payment_form')