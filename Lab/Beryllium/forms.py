from django import forms
from django.forms.fields import Field
from django.forms.models import ModelForm
from django.forms.widgets import HiddenInput
from .models import Patient, Test, Tester, Well, Material
from django.forms.widgets import NumberInput


class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'tester', 'patient', 'date', 'description']
    name = forms.CharField()
        
    date = forms.DateField(widget=NumberInput(attrs={'type': 'date'}))

class WellForm(forms.ModelForm):
    class Meta:
        model = Well
        fields = ['isActive', 'material', 'dosage', 'unitOfMeasure']
