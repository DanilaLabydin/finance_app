from django import forms
from .models import FoodProducts, Stuff, SStuff, FFoodProducts, Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]

        
class FoodProductsForm(forms.ModelForm):
    class Meta:
        model = FoodProducts
        fields = ["title", "amount", "price", "date"]


class StuffForm(forms.ModelForm):
    class Meta:
        model = Stuff
        fields = ["title", "price", "date"]


class SStuffForm(forms.ModelForm):
    class Meta:
        model = SStuff
        fields = ["title", "price", "date"]


class FFoodForm(forms.ModelForm):
    class Meta:
        model = FFoodProducts
        fields = ["title", "price", "amount", "date"]
