from django import forms
from django.forms import ModelForm
from .models import EmpDetails

class EmpDetailsForm(forms.ModelForm):  
    class Meta:  
        model = EmpDetails
        fields = "__all__"  