from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView # Add this import
from django.conf import settings # Add this import
from django.conf.urls.static import static # Add this import

urlpatterns = [

    path('', include('website.urls')),

    path('patient/', include('patient.urls')),

    path('doctor/', include('doctor.urls')),

    path('appointment/', include('appointment.urls')),

    path('prescription/', include('prescription.urls')),

    path('admin/', admin.site.urls),
    
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.png', permanent=True)),
    path('favicon.png', RedirectView.as_view(url='/static/favicon.png', permanent=True))

]