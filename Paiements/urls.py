from django.urls import path
from .views import Payment , Card_Payment
urlpatterns = [
    path('<int:id>',Payment.as_view(),name="paiment-direct"),
    path('payment-card/<int:quantite>/<str:coupon>/<str:price>/',Card_Payment.as_view(),name="checkout"),
]
