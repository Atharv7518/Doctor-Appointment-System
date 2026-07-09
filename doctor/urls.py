from django.urls import path
from . import views

urlpatterns = [

    path('register/', views.register, name='doctor_register'),

    path('login/', views.login_view, name='doctor_login'),

    path('dashboard/', views.dashboard, name='doctor_dashboard'),

    path('logout/', views.logout_view, name='doctor_logout'),

]