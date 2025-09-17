from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.views import View
from django.contrib import messages

class AuthView(View):
    """
    Vue unifiée pour l'authentification (login + register)
    """
    template_name = 'accounts/auth.html'
    
    def get(self, request):
        context = {
            'login_form': AuthenticationForm(),
            'register_form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    
    def post(self, request):
        # Déterminer quel formulaire a été soumis
        if 'login-submit' in request.POST:
            return self._handle_login(request)
        elif 'register-submit' in request.POST:
            return self._handle_register(request)
        
        return redirect('auth')
    
    def _handle_login(self, request):
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Bienvenue {user.username} !")
            return redirect('dashboard')
        
        # Réafficher avec erreurs
        context = {
            'login_form': form,
            'register_form': UserCreationForm()
        }
        return render(request, self.template_name, context)
    
    def _handle_register(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Compte créé avec succès !")
            return redirect('dashboard')
        
        # Réafficher avec erreurs
        context = {
            'login_form': AuthenticationForm(),
            'register_form': form
        }
        return render(request, self.template_name, context)