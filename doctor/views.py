from django.shortcuts import render,redirect
from .models import Doctor
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

    if 'doctor_id' not in request.session:

        return redirect('doctor_login')

    return render(

        request,

        'doctor/dashboard.html',

        {

            'name':request.session['doctor_name']

        }

    )
    
def logout_view(request):

    request.session.flush()

    return redirect('doctor_login')
