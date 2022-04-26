from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FoodProducts, Rest
from django.views.generic import CreateView
from .forms import FoodProductsForm, RestForm


def index(request):
    return render(request, 'finance_app/index.html')


def items_list(request):
    food_products = FoodProducts.objects.raw('SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts')
    context = {'food_products': food_products}
    return render(request, 'finance_app/items_list.html', context)


def rests_list(request):
    rests = Rest.objects.all()
    headers = ['title', 'amount', 'price', 'date']
    context = {'rests': rests, 'headers': headers}
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
        form = RestForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, 'finance_app/add_rest.html', context)


def test(request):
    headers = ['date', 'a', 'b', 'c']
    body = [{'date': '2015-10-16', 'a': 1, 'b': 2, 'c': 3},
            {'date': '2015-10-17', 'a': 4, 'b': 5, 'c': 6}]
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/test.html', context)
