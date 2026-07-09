from django.shortcuts import render, redirect
from .models import Patient

def register(request):

    if request.method == "POST":

        Patient.objects.create(

            first_name=request.POST['first_name'],

            last_name=request.POST['last_name'],

            gender=request.POST['gender'],

            dob=request.POST['dob'],

            phone=request.POST['phone'],

            email=request.POST['email'],

            password=request.POST['password'],

            address=request.POST['address']

        )

        return render(request, 'patient/register.html', {
            'success': 'Registration Successful!'
        })

    return render(request, 'patient/register.html')

def login_view(request):

    if request.method == "POST":

        email = request.POST['email']
        password = request.POST['password']

        patient = Patient.objects.filter(
            email=email,
            password=password
        ).first()

        if patient:

            request.session['patient_id'] = patient.patient_id
            request.session['patient_name'] = patient.first_name

            return redirect('dashboard')

        else:

            return render(
                request,
                'patient/login.html',
                {'error': 'Invalid Email or Password'}
            )

    return render(request, 'patient/login.html')

def dashboard(request):

    if 'patient_id' not in request.session:

        return redirect('login')

    return render(
        request,
        'patient/dashboard.html',
        {
            'name': request.session['patient_name']
        }
    )
    
def logout_view(request):

    request.session.flush()

    return redirect('login')

