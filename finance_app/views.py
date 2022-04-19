from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FoodProducts
from django.views.generic import CreateView
from .forms import FoodProductsForm


def index(request):
    food_products = FoodProducts.objects.all()
    print(food_products)
    context = {'food_products': food_products}
    return render(request, 'finance_app/index.html', context)





def add_item(request):
    if request.method != 'POST':
        form = FoodProductsForm()
    else:
        form = FoodProductsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'finance_app/add_item_form.html', context)
