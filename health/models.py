from django.db import models

# Create your models here.


# Writing Abstract Class (Doctor), and classes for each Field of Medicine
# SOLID

class Doctor(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    full_name = models.CharField(max_length=100)
    field = models.CharField(max_length=20)
    email = models.EmailField()
    brief_information = models.CharField(max_length=50)
    profile_information = models.CharField(max_length=1000)
    scientific_degree = models.CharField(max_length=50)
    profile_image = models.ImageField()

    def __str__(self):
        return self.full_name




# Writing condition Section class

class Condition(models.Model):

    field = models.CharField(max_length=30)
    name = models.CharField(max_length=50)
    brief_description = models.CharField(max_length=50)
    first_paragraph = models.CharField(max_length=100)
    second_paragraph = models.CharField(max_length=100)
    third_paragraph = models.CharField(max_length=100)
    question_one = models.CharField(max_length=50)
    question_two = models.CharField(max_length=50)
    question_three = models.CharField(max_length=50)
    answer_one = models.CharField(max_length=200)
    answer_two = models.CharField(max_length=200)
    answer_three = models.CharField(max_length=200)
    condition_image = models.ImageField()

    def __str__(self):
        return self.name
    
    

class Booking(models.Model):
    email= models.EmailField(max_length=100)
    patient_first_name= models.CharField(max_length=30)
    patient_last_name= models.CharField(max_length=30)
    age = models.IntegerField()
    speciality_field = models.CharField(max_length=30)
    condition_field = models.CharField(max_length=30)


    def __str__(self):
        return self.condition_field