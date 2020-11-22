# creating form using form
from django.core import validators
from django import forms
from .models import User


class StudentRegistrations(forms.ModelForm):
    class Meta:
        model=User
        fields=['name','email','password']
        # for adding html property such as class type and id etc
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password':forms.PasswordInput(attrs={'class':'form-control'})
        }