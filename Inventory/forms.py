from django import forms
from .models import *

class Product_form(forms.ModelForm):
    class Meta:
        model=Product
        fields="__all__"