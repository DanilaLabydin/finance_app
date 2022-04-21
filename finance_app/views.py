from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FoodProducts, Rest
from django.views.generic import CreateView
from .forms import FoodProductsForm, RestForm


def index(request):
    return render(request, 'finance_app/index.html')


def items_list(request):
    # food_products = FoodProducts.objects.all()
    food_products = FoodProducts.objects.raw('SELECT id, title, amount, price, date, amount*price as A FROM finance_app_foodproducts')
    # print(food_products)
    context = {'food_products': food_products}
    return render(request, 'finance_app/items_list.html', context)


def rests_list(request):
    # food_products = FoodProducts.objects.all()
    rests = Rest.objects.raw('SELECT id, title, amount, price, date, amount*price as A FROM finance_app_rest')
    # print(food_products)
    context = {'rests': rests}
    return render(request, 'finance_app/rests_list.html', context)


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


def add_rest(request):
    if request.method != 'POST':
        form = RestForm()
    else:
        form = FoodProductsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'finance_app/add_item_form.html', context)