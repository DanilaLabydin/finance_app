from django import forms
from .models import FoodProducts, Stuff


class FoodProductsForm(forms.ModelForm):
    class Meta:
        model = FoodProducts
        fields = ['title', 'amount', 'price', 'date']


class StuffForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = ['title', 'price', 'date']
