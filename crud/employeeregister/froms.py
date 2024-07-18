from .models import EmployeeData
from django import forms

class EmployeeRegister(forms.ModelForm):
    class Meta:
        model = EmployeeData
        # fields = ['name','email','department','contact','address','image']
        fields = '__all__'
        widgets = {
            'name' : forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'department' : forms.TextInput(attrs={'class':'form-control'}),
            'contact' : forms.TextInput(attrs={'class':'form-control'}),
            'address' : forms.TextInput(attrs={'class':'form-control'}),
        }