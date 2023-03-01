from django.urls import path

from . import views

urlpatterns = [
    path('home', views.index, name='index'),
    path('braintumor', views.brain_tumor, name=''),
    path('ourdoctors', views.our_doctors, name=''),
    path('doctorsignup', views.doctor_signup, name=''),
    path('patientsignup', views.patient_signup  , name=''),
    path('vision', views.vision, name='')
]