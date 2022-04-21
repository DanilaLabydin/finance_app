from django import forms
from .models import FoodProducts, Rest


class FoodProductsForm(forms.ModelForm):
    class Meta:
        model = FoodProducts
        fields = ['title', 'amount', 'price', 'date']


class RestForm(forms.ModelForm):
    class Meta:
        model = Rest
        fields = ['title', 'amount', 'price', 'date']
