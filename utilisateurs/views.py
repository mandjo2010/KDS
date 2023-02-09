from django.shortcuts import render, redirect
from utilisateurs.forms import UserRegistrationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.conf import settings


User = settings.AUTH_USER_MODEL


# Create your views here.
def register(request):
        if request.method == "POST":
                form = UserRegistrationForm(request.POST or None)
                if form.is_valid:
                        new_user = form.save()
                        username = form.cleaned_data.get("username")
                        messages.success(
                        request, f"Bonjour {username}, votre compte utilisateur a été crée avec succès")
                        new_user = authenticate(username=form.cleaned_data['email'],
                                                password=form.cleaned_data['password1']
                                                )
                        login(request, new_user)
                        return redirect("accueil:accueil")
        else:
                print("User cannot not be registred")
                form = UserRegistrationForm()
        context = {
        'form': form,
        }
        return render(request, "utilisateurs/register.html", context)


def login(request):
        if request.user.is_authenticated:
                messages.warning(request, f"Vous êtes déjà  connecté")
                return redirect("accueil:accueil")

        if request.method == "POST":
                email = request.POST.get("email")
                password = request.POST.get("password")

                try:
                        user = User.objects.get(email=email)
                        user = authenticate(request, email=email, password=password)

                        if user is not None:
                                login(request, user)
                                messages.success(request, "Vous êtes déjà  connecté.")
                                return redirect("accueil:accueil")
                        else:
                                messages.warning(request, "Cet utilisateur n'existe pas. Créer un compte")
                except:
                        messages.warning(request, f" l'email {email} n'existe pas")

        context = {

                }
        return render(request, "utilisateurs/signin.html", context)


def logout(request):
        logout(request)
        messages.success(request, "Vous-vous êtes  deconnecté")
        return redirect("utilisateurs:login")
