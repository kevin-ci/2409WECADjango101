from django import forms
from .models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['date', 'time', 'doctor_type']
        widgets = {
            'date': forms.DateInput(attrs={'readonly': 'readonly'}),
            'time': forms.TimeInput(attrs={'readonly': 'readonly'}),
        }