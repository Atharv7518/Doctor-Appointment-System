from django.urls import path
from . import views

urlpatterns = [

    path('book/', views.book_appointment, name='book_appointment'),

    path('my-appointments/', views.my_appointments, name='my_appointments'),

    path('doctor-appointments/', views.doctor_appointments, name='doctor_appointments'),

    path('approve/<int:id>/', views.approve_appointment, name='approve'),

    path('reject/<int:id>/', views.reject_appointment, name='reject'),

    path('complete/<int:id>/', views.complete_appointment, name='complete'),

]