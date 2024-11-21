from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    description = models.TextField()

    def __str__(self):
        return f"Cita de {self.user.username} para el {self.date} a las {self.time}"
        return f"{self.date} {self.time} - Disponible: {self.is_available}"