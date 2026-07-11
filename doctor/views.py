from django.shortcuts import render,redirect
from .models import Doctor
from datetime import date
from appointment.models import Appointment



def register(request):

    if request.method=="POST":
        
        print(request.POST)

        Doctor.objects.create(

    first_name=request.POST.get('first_name'),

    last_name=request.POST.get('last_name'),

    gender=request.POST.get('gender'),

    specialization=request.POST.get('specialization'),

    qualification=request.POST.get('qualification'),

    experience=request.POST.get('experience'),

    phone=request.POST.get('phone'),

    email=request.POST.get('email'),

    password=request.POST.get('password'),

    consultation_fee=request.POST.get('consultation_fee'),

    available_days=request.POST.get('available_days'),

    available_time=request.POST.get('available_time'),

)

        return render(
            request,
            'doctor/register.html',
            {
                'success':'Doctor Registered Successfully'
            }
        )

    return render(request,'doctor/register.html')

def login_view(request):

    if request.method=="POST":

        email=request.POST['email']

        password=request.POST['password']

        doctor=Doctor.objects.filter(

            email=email,

            password=password

        ).first()

        if doctor:

            request.session['doctor_id']=doctor.doctor_id

            request.session['doctor_name']=doctor.first_name

            return redirect('doctor_dashboard')

        else:

            return render(

                request,

                'doctor/login.html',

                {

                    'error':'Invalid Email or Password'

                }

            )

    return render(request,'doctor/login.html')

def dashboard(request):
    # Check if doctor is logged in
    if 'doctor_id' not in request.session:
        return redirect('doctor_login')

    # Get the logged-in doctor's object
    doctor_id = request.session['doctor_id']
    doctor = Doctor.objects.get(doctor_id=doctor_id)

    # 1. Count Today's Visits (Matching today's date)
    today_visits_count = Appointment.objects.filter(
        doctor=doctor, 
        appointment_date=date.today()
    ).count()

    # 2. Count Completed Appointments
    completed_count = Appointment.objects.filter(
        doctor=doctor, 
        status='Completed'
    ).count()

    # 3. Count Pending Appointments
    pending_count = Appointment.objects.filter(
        doctor=doctor, 
        status='Pending'
    ).count()

    # Send the real data to the template
    return render(
        request,
        'doctor/dashboard.html',
        {
            'name': request.session['doctor_name'],
            'today_visits': today_visits_count,
            'completed': completed_count,
            'pending': pending_count
        }
    )
    
def logout_view(request):

    request.session.flush()

    return redirect('doctor_login')
