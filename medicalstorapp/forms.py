from django import forms
from .models import medicalstore

class medicalform(forms.ModelForm):
    class Meta:
        model = medicalstore
        fields = '__all__'