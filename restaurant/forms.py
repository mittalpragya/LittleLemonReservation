from .models import *
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'