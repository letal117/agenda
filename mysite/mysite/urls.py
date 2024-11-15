from django.contrib import admin
from django.urls import path, include  # Incluye 'include' para incluir las urls de apps

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),  # Ruta para la aplicación accounts
]
