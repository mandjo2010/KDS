from django import forms
from django.contrib.auth.forms import UserCreationForm
from utilisateurs.models import User


class UserRegistrationForm(UserCreationForm):
        # prénom = forms.CharField(
        #         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prénom'}))

        # nom = forms.CharField(
        #         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}))

        username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Pseudonyme'}))
        email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
        password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de Passe'}))
        password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmez votre Mot de Passe'}))

        class Meta:
                model = User
                fields = ('username', 'email', )
