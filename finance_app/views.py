from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodProducts


def index(request):
    food_products = FoodProducts.objects.all()
    context = {'food_products': food_products}
    return render(request, 'finance_app/index.html', context)

