from django import forms
from .models import Customer,Order

class Customer_form(forms.ModelForm):
    class Meta:
        model=Customer
        fields="__all__"
        
class Order_form(forms.ModelForm):
    class Meta:
        model=Order
        fields=['customer_reference','product_reference','order_number','order_date','quantity']