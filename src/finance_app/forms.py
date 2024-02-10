from django import forms
from .models import Category, Spent


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name", "description"]


class SpentForm(forms.ModelForm):
    class Meta:
        model = Spent
        fields = ["name", "price", "description", "category"]
