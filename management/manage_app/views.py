
from django.shortcuts import render, get_object_or_404, redirect
from .models import Patient, Doctor, Appointment, Billing
from .forms import PatientForm, DoctorForm, AppointmentForm, BillingForm

def home(request):
    return render(request, 'manage_app/home.html')

def patient_list(request):
    patients = Patient.objects.all()
    return render(request, 'manage_app/patient_list.html', {'patients': patients})

def doctor_list(request):
    doctors = Doctor.objects.all()
    return render(request, 'manage_app/doctor_list.html', {'doctors': doctors})

def appointment_list(request):
    appointments = Appointment.objects.all()
    return render(request, 'manage_app/appointment_list.html', {'appointments': appointments})

def billing_list(request):
    bills = Billing.objects.all()
    return render(request, 'manage_app/billing_list.html', {'bills': bills})