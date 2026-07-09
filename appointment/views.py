from django.shortcuts import render, redirect
from django.contrib import messages

from patient.models import Patient
from doctor.models import Doctor
from .models import Appointment
from datetime import date

def book_appointment(request):

    if 'patient_id' not in request.session:
        return redirect('login')

    specialization = request.GET.get('specialization')

    if specialization:
        doctors = Doctor.objects.filter(
            specialization=specialization
        )
    else:
        doctors = Doctor.objects.all()

    if request.method == "POST":

        appointment_date = request.POST.get('appointment_date')

        # Validation
        from datetime import date

        if appointment_date < str(date.today()):

            return render(
                request,
                'appointment/book.html',
                {
                    'doctors': doctors,
                    'error': 'Past date is not allowed.'
                }
            )

        patient = Patient.objects.get(
            patient_id=request.session['patient_id']
        )

        doctor = Doctor.objects.get(
            doctor_id=request.POST.get('doctor')
        )

        Appointment.objects.create(

            patient=patient,

            doctor=doctor,

            appointment_date=appointment_date,

            appointment_time=request.POST.get('appointment_time'),

            symptoms=request.POST.get('symptoms')

        )

        messages.success(
            request,
            "Appointment Booked Successfully"
        )

        return redirect('my_appointments')

    return render(
        request,
        'appointment/book.html',
        {
            'doctors': doctors
        }
    )
    
def my_appointments(request):

    patient = Patient.objects.get(

        patient_id=request.session['patient_id']

    )

    appointments = Appointment.objects.filter(

        patient=patient

    )

    return render(

        request,

        'appointment/my_appointments.html',

        {

            'appointments': appointments

        }

    )
    
def approve_appointment(request, id):

    appointment = Appointment.objects.get(
        appointment_id=id
    )

    appointment.status = "Approved"

    appointment.save()

    return redirect('doctor_appointments')

def doctor_appointments(request):

    if 'doctor_id' not in request.session:

        return redirect('doctor_login')

    doctor = Doctor.objects.get(
        doctor_id=request.session['doctor_id']
    )

    appointments = Appointment.objects.filter(
        doctor=doctor
    )

    return render(
        request,
        'appointment/doctor_appointments.html',
        {
            'appointments': appointments
        }
    )
    
    
def reject_appointment(request, id):

    appointment = Appointment.objects.get(
        appointment_id=id
    )

    appointment.status = "Rejected"

    appointment.save()

    return redirect('doctor_appointments')

def complete_appointment(request, id):

    appointment = Appointment.objects.get(
        appointment_id=id
    )

    appointment.status = "Completed"

    appointment.save()

    return redirect('doctor_appointments')