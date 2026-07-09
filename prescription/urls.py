from django.urls import path
from . import views

urlpatterns = [

    path(
        'write/<int:appointment_id>/',
        views.write_prescription,
        name='write_prescription'
    ),

    path(
        'view/',
        views.view_prescription,
        name='view_prescription'
    ),
    
    path(
    'download/<int:id>/',
    views.download_prescription,
    name='download_prescription'
    ),

]