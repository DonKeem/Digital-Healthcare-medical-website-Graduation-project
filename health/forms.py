from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['patient_first_name', 'patient_last_name', 'age', 'speciality_field', 'condition_field']

    def __init__(self, *args, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        # Customize form labels or add additional attributes if needed
        self.fields['patient_first_name'].label = 'Patient First Name'
        self.fields['patient_last_name'].label = 'Patient Last Name'
        self.fields['speciality_field'].label = 'Speciality'
        self.fields['condition_field'].label = 'Condition'
        self.fields['age'].widget.attrs['min'] = 0  # Set a minimum value for age

        # You may also hide the 'email' field as it will be retrieved from the logged-in user
        self.fields['email'].widget = forms.HiddenInput()

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise forms.ValidationError("Age cannot be negative.")
        return age
