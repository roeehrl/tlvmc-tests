from django import forms
from django.forms.fields import Field
from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput
from .models import Patient, Test, Tester, Well, Material

class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'tester', 'patient', 'date', 'description']

class WellForm(forms.ModelForm):
    class Meta:
        model = Well
        fields = ['isActive', 'material', 'dosage', 'unitOfMeasure']
