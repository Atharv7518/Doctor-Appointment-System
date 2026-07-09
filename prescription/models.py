from django.db import models
from appointment.models import Appointment

class Prescription(models.Model):

    prescription_id = models.AutoField(primary_key=True)

    appointment = models.OneToOneField(
        Appointment,
        on_delete=models.CASCADE
    )

    diagnosis = models.TextField()

    medicines = models.TextField()

    dosage = models.TextField()

    advice = models.TextField()

    next_visit = models.DateField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return f"Prescription #{self.prescription_id}"