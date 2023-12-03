from django.shortcuts import render
from health.models import Condition, Doctor
from django.http import HttpResponse




# Create your views here.


def index(request):

    condition_blogs = Condition.objects.all()


    return render(request, "index.html", {'condition_blogs':condition_blogs})



def our_doctors(request):

    doctors = Doctor.objects.all()

    return render(request, 'ourdoctors.html', {'doctors': doctors})



def vision(request):
    return render(request, 'vision.html')


def doctor_profile(request,doctor_id):

    desired_doctor = Doctor.objects.get(id = doctor_id)


    return render(request, 'doctorprofile.html', {'desired_doctor': desired_doctor})


def condition(request,cond_id):

    desired_condition = Condition.objects.get(id = cond_id)
    condition_field = desired_condition.field
    condition_doctors = Doctor.objects.filter(field = condition_field )
    
    context = {'condition_doctors': condition_doctors, 'desired_condition': desired_condition}


    return render(request, 'condition.html', context)



def booking(request):
    return render(request, 'bookingform.html')