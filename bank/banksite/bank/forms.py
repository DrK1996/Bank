from django import forms
from .models import District, Branch

class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    age = forms.IntegerField()
    phone_number = forms.CharField()
    email = forms.EmailField()
    address = forms.CharField(max_length=255)
    district = forms.ModelChoiceField(queryset=District.objects.all())
    branch = forms.ModelChoiceField(queryset=Branch.objects.all())

