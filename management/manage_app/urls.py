from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('patients/', views.patient_list, name='patient_list'),
    path('doctors/', views.doctor_list, name='doctor_list'),
    path('appointments/', views.appointment_list, name='appointment_list'),
    path('billing/', views.billing_list, name='billing_list'),
]