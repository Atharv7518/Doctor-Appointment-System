from django.db import models


class Patient(models.Model):

    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    ]

    patient_id = models.AutoField(primary_key=True)

    first_name = models.CharField(max_length=50)

    last_name = models.CharField(max_length=50)

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    dob = models.DateField()

    phone = models.CharField(max_length=15)

    email = models.EmailField(unique=True)

    password = models.CharField(max_length=255)

    address = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"