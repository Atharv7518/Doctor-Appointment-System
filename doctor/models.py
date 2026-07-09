from django.db import models


class Doctor(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    SPECIALIZATION_CHOICES = [
        ('Cardiologist', 'Cardiologist'),
        ('Dermatologist', 'Dermatologist'),
        ('Neurologist', 'Neurologist'),
        ('Orthopedic', 'Orthopedic'),
        ('Pediatrician', 'Pediatrician'),
        ('Dentist', 'Dentist'),
        ('General Physician', 'General Physician'),
    ]

    doctor_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    specialization = models.CharField(
        max_length=100,
        choices=SPECIALIZATION_CHOICES
    )

    qualification = models.CharField(max_length=100)

    experience = models.PositiveIntegerField()

    phone = models.CharField(max_length=15)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=255)

    consultation_fee = models.DecimalField(
        max_digits=8,
        decimal_places=2
    )

    available_days = models.CharField(max_length=100)

    available_time = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"