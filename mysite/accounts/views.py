from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy

# Vista de Login (LoginView de Django)
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # La plantilla HTML que creamos
    next_page = reverse_lazy('accounts:home')  # Redirigir a 'home' después del inicio de sesión exitoso

# Vista de Registro de Usuario
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cuenta creada exitosamente!')
            return redirect('accounts:home')  # Redirigir al home después del registro
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

# Vista Principal (Home)
def home_view(request):
    return render(request, 'accounts/home.html')
