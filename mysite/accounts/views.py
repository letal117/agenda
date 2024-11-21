from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .forms import AppointmentForm  # Asegúrate de importar tu formulario de citas
from .models import Appointment

# Vista de Login (LoginView de Django)
class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    next_page = reverse_lazy('accounts:home')  # Redirigir tras iniciar sesión

# Vista de Registro de Usuario
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Cuenta creada exitosamente!')
            return redirect('accounts:home')  # Redirigir al home
    else:
        form = UserCreationForm()

    return render(request, 'accounts/signup.html', {'form': form})

# Vista Principal (Home) con formulario de agendar cita
@login_required
def home_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Guardar la cita en la base de datos
            appointment = form.save(commit=False)
            appointment.user = request.user  # Asignar el usuario actual a la cita
            appointment.save()
            messages.success(request, 'Cita agendada exitosamente!')
            return redirect('accounts:home')  # Redirigir al home después de agendar la cita
    else:
        form = AppointmentForm()

    return render(request, 'accounts/home.html', {'form': form})
