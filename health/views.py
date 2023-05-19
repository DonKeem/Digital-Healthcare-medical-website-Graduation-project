from django.shortcuts import render
from .models import Condition, Doctor
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
import tensorflow as tf
import numpy as np
from django.template.response import TemplateResponse
from django.conf import settings
import cv2
import os
from . import crop_imgs



# Create your views here.


def index(request):

    condition_blogs = Condition.objects.all()


    return render(request, "index.html", {'condition_blogs':condition_blogs})


class CustomFileSystemStorage(FileSystemStorage):
    def get_available_name(self, name, max_length=None):
        self.delete(name)
        return name


def brain_tumor(request):
    if request.method == "POST":
        message = ""
        prediction = ""
        fss = CustomFileSystemStorage()
        image = request.FILES["image"]
        print("Name", image.file)
        _image = fss.save(image.name, image)
        path = str(settings.MEDIA_ROOT) + "/" + image.name
        print("Path", path)
        # image details
        image_url = fss.url(_image)
        # Read the image
        imag = cv2.imread(path)
        print("Image shape:", imag.shape)
        print("Image channels:", imag.shape[2])

        imag = cv2.resize(imag, (224, 224))
        print("Image1 shape:", imag.shape)
        imag2 = crop_imgs.crop_img(imag)
        
        print("Image2 shape:", imag2.shape)
        imag3 = crop_imgs.preprocess_img(imag2, (224, 224))
        print("Image3 shape:", imag3.shape)
        imag3 = np.expand_dims(imag3, axis=0)

        # load model
        model = tf.keras.models.load_model(os.getcwd() + '/models/CNN.h5')
        print("Model", model)
        score_predict = model.predict(imag3)
        print("Score Predict shape:", score_predict.shape)
        print("Score Predict", score_predict)
        predictions = [1 if x > 0.5 else 0 for x in score_predict]
        print("Prediction", predictions)

        if predictions[0] == 0:
            prediction = "You don't have brain tumor"
        elif predictions[0] == 1:
            prediction = "You have brain tumor"
        else:
            prediction = "Error"

        return TemplateResponse(
            request,
            "result.html",
            {
                "message": message,
                "image_url": image_url,
                "prediction": prediction,
            },
        )
    else:
        return render(request, "braintumor.html")




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