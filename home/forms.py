from django import forms
from django import forms

from .models import Booking,Contact

class DateInput(forms.DateInput):
    input_type = 'date'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'

        widgets = {
            'booking_date' : DateInput(),
        }
        labels = {
            'p_name': "Patient Name: ",
            'p_phone': "Patient Phone: ",
            'p_email': "Patient Email: ",
            'doc_name': "Doctor Name: ",
            'booking_date': "Booking Date: ",
            
        }

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

        labels = {
            'f_name' : "First Name: ",
            'l_name' : "Last Name: ",
            'email' : "Email: ",
            'phone' : "Phone: ",
            'remark' : "Remark: ",
        }

