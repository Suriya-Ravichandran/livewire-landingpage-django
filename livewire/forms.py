from django import forms
from .models import Enroll

class EnrollForm(forms.ModelForm):
    name = forms.CharField(max_length=200,required=True)
    email = forms.EmailField(max_length=200,required=True)
    phone = forms.CharField(max_length=15,required=True)
    address = forms.CharField(max_length=500,required=True)
    course = forms.CharField(max_length=50,required=True)
    
    class Meta:
        model = Enroll
        fields = [
            "name",
            "email",
            "phone",
            "address",
            "course",
            "adhaarcard",
            "photo",
        ]

