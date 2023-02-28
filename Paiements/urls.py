from django.urls import path
from .views import Payment , Card_Payment , payment_process
urlpatterns = [
    path('<int:id>',Payment.as_view(),name="paiment-direct"),
    path('payment-card/<int:quantite>/<str:coupon>/<str:price>/<int:id>/',Card_Payment.as_view(),name="checkout"),
    path('stripe-payment',payment_process , name="payment_process")
]
