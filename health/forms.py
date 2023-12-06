from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['patient_first_name', 'patient_last_name', 'age', 'speciality_field', 'condition_field']

    
    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise forms.ValidationError("Age cannot be negative.")
        return age
