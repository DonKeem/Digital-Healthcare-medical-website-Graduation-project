from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse


def index(request):
    return render(request, "index.html")





def brain_tumor(request):
    return render(request, 'BrainTumor.html')



def our_doctors(request):
    return render(request, 'ourdoctors.html')



def doctor_signup(request):
    return render(request, 'doctorssignup.html')


def patient_signup(request):
    return render(request, 'patientssignup.html')



def vision(request):
    return render(request, 'vision.html')