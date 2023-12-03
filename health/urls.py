from django.urls import path

from . import views


app_name = 'health'

urlpatterns = [
    path('', views.index, name='index'),
    path('ourdoctors', views.our_doctors, name='our_doctors'),
    path('vision', views.vision, name='vision'),
    path('doctor/<int:doctor_id>/', views.doctor_profile, name='doctor_profile'),
    path('condition/<int:cond_id>/', views.condition, name='condition'),
    path('booking', views.booking, name="booking"),
    ]
