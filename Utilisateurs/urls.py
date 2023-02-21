from django.urls import path
from .views import loginView , RegisterView , logout_view
urlpatterns = [
    path('login',loginView.as_view(),name='loginPage'),
    path('signup',RegisterView.as_view(),name='registerPage'),
    path('logout/',logout_view, name='logout')
]
