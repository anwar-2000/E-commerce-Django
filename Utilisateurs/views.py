from django.shortcuts import render 
from django.contrib.auth.views import LoginView 
from django.contrib.auth import logout
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm
from Utilisateurs.models import Utilisateur

def logout_view(request):
    if  request.user.is_authenticated :
        logout(request)
        return reverse_lazy('accueil:index')
    return reverse_lazy('accueil:index')


class loginView(LoginView):
    template_name="Utilisateurs/login.html"

    def get_success_url(self):
        # Redirect to another app URL after a successful login
        return reverse_lazy('accueil:index')

class UtilisateurCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = Utilisateur
        fields = ('email', 'password1', 'password2', 'mobile', 'addresse_de_livraison')

class RegisterView(CreateView):
    template_name = 'Utilisateurs/register.html'
    success_url = reverse_lazy('loginPage')
    form_class = UtilisateurCreationForm

"""
    class RegisterView(CreateView):
    template_name="Utilisateurs/register.html"
    success_url = reverse_lazy("loginPage")
    model = Utilisateur

    def form_valid(self, form):
        response = super().form_valid(form)
        email = form.cleaned_data.get('email')
        password = form.cleaned_data.get('password1')
        user = authenticate(email=email, password=password)
        login(self.request, user)
        return HttpResponseRedirect(self.success_url)
"""
