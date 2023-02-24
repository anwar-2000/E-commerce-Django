from django.urls import path


from .views import AllProduct , Productdetail , ProductByCategory
urlpatterns = [
    path('',AllProduct.as_view(),name='allProducts'),
    path('<str:category>/',ProductByCategory.as_view(),name='categoryProductPage'),
    path('<int:pk>',Productdetail.as_view(),name='produitDetails-page')
]
