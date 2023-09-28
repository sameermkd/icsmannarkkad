from django import forms
from .models import Data

class DateInput(forms.DateInput):
    input_type = 'date'

class DataForm(forms.ModelForm):
    class Meta:
        model = Data
        fields = '__all__'
        widgets = {
            'date': DateInput()
        }
        labels = {
            'invoiceno': 'Invoice No',
            'date': 'Select Date',
            'subject': 'Select Subject',
            'report': 'Enter Class Report',
        }