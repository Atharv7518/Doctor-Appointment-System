from django.urls import path
from . import views

urlpatterns = [

    path('', views.landing, name='landing'),

    path('home/', views.home, name='home'),

    path('login/', views.login_page, name='common_login'),

    path('register/', views.register_page, name='common_register'),

]