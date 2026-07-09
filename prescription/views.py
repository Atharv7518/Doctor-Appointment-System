from django.shortcuts import render, redirect

from .models import Prescription

from appointment.models import Appointment

from django.http import HttpResponse

from reportlab.pdfgen import canvas

def write_prescription(request, appointment_id):

    appointment = Appointment.objects.get(
        appointment_id=appointment_id
    )

    if request.method == "POST":

        Prescription.objects.create(

            appointment=appointment,

            diagnosis=request.POST['diagnosis'],

            medicines=request.POST['medicines'],

            dosage=request.POST['dosage'],

            advice=request.POST['advice'],

            next_visit=request.POST['next_visit']

        )

        appointment.status = "Completed"

        appointment.save()

        return redirect('doctor_appointments')

    return render(

        request,

        'prescription/write.html',

        {

            'appointment': appointment

        }

    )
    
def view_prescription(request):

    prescriptions = Prescription.objects.filter(
        appointment__patient_id=request.session['patient_id']
    )

    return render(
        request,
        'prescription/view.html',
        {
            'prescriptions': prescriptions
        }
    )
    
    
def download_prescription(request, id):

    prescription = Prescription.objects.get(
        prescription_id=id
    )

    response = HttpResponse(
        content_type='application/pdf'
    )

    response['Content-Disposition'] = (
        f'attachment; filename="Prescription_{id}.pdf"'
    )

    pdf = canvas.Canvas(response)

    pdf.setFont("Helvetica-Bold", 18)
    pdf.drawString(180, 800, "Doctor Appointment System")

    pdf.setFont("Helvetica", 12)

    pdf.drawString(
        50,
        760,
        f"Patient : {prescription.appointment.patient.first_name} {prescription.appointment.patient.last_name}"
    )

    pdf.drawString(
        50,
        740,
        f"Doctor : Dr. {prescription.appointment.doctor.first_name} {prescription.appointment.doctor.last_name}"
    )

    pdf.drawString(
        50,
        720,
        f"Diagnosis : {prescription.diagnosis}"
    )

    pdf.drawString(
        50,
        700,
        f"Medicines : {prescription.medicines}"
    )

    pdf.drawString(
        50,
        680,
        f"Dosage : {prescription.dosage}"
    )

    pdf.drawString(
        50,
        660,
        f"Advice : {prescription.advice}"
    )

    pdf.drawString(
        50,
        640,
        f"Next Visit : {prescription.next_visit}"
    )

    pdf.save()

    return response
