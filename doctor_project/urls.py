from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('', include('website.urls')),

    path('patient/', include('patient.urls')),

    path('doctor/', include('doctor.urls')),

    path('appointment/', include('appointment.urls')),

    path('prescription/', include('prescription.urls')),

    path('admin/', admin.site.urls),

]