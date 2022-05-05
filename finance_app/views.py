import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FoodProducts, Rest, Stuff
from django.views.generic import CreateView
from .forms import FoodProductsForm, StuffForm


def index(request):
    return render(request, 'finance_app/index.html')


def items_list(request):
    food_products = FoodProducts.objects.raw('SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts')
    headers = ['title', 'amount', 'price', 'total', 'date']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list.html', context)


def stuff_list(request):
    stuff = Stuff.objects.all()
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ['title', 'price', 'date']
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/stuff_list.html', context)


def add_item(request):
    if request.method != 'POST':
        form = FoodProductsForm()
    else:
        form = FoodProductsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('items_list')

    context = {'form': form}
    return render(request, 'finance_app/add_item.html', context)


def add_stuff(request):
    if request.method != 'POST':
        form = StuffForm
    else:
        form = StuffForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('stuff_list')

    context = {'form': form}
    return render(request, 'finance_app/add_stuff.html', context)


# sorting the stuff
def stuff_order_price_asc(request):
    stuff = Stuff.objects.order_by('price')
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ['title', 'price', 'date']
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/stuff_list.html', context)


def stuff_order_price_desc(request):
    stuff = Stuff.objects.order_by('-price')
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ['title', 'price', 'date']
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/stuff_list.html', context)


def stuff_order_title_asc(request):
    stuff = Stuff.objects.order_by('title')
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ['title', 'price', 'date']
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/stuff_list.html', context)


def stuff_order_title_desc(request):
    stuff = Stuff.objects.order_by('-title')
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ['title', 'price', 'date']
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/stuff_list.html', context)


def stuff_order_date_asc(request):
    stuff = Stuff.objects.order_by('date')
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ['title', 'price', 'date']
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/stuff_list.html', context)


def stuff_order_date_desc(request):
    stuff = Stuff.objects.order_by('-date')
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ['title', 'price', 'date']
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/stuff_list.html', context)


# stuff group by title
def stuff_group_title_asc(request):
    stuff = Stuff.objects.raw('SELECT id, title, sum(price) as total FROM finance_app_stuff GROUP BY title ORDER BY title')
    body = []
    for i in stuff:
        body.append(dict(title=i.title, total=i.total))
    headers = ['title', 'total']
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/stuff_group_title.html', context)


def stuff_group_title_desc(request):
    stuff = Stuff.objects.raw('SELECT id, title, sum(price) as total FROM finance_app_stuff GROUP BY title ORDER BY title DESC')
    body = []
    for i in stuff:
        body.append(dict(title=i.title, total=i.total))
    headers = ['title', 'total']
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/stuff_group_title.html', context)


def stuff_group_title_total_desc(request):
    stuff = Stuff.objects.raw('SELECT id, title, sum(price) as total FROM finance_app_stuff GROUP BY title ORDER BY total DESC')
    body = []
    for i in stuff:
        body.append(dict(title=i.title, total=i.total))
    headers = ['title', 'total']
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/stuff_group_title.html', context)


def stuff_group_title_total_asc(request):
    stuff = Stuff.objects.raw('SELECT id, title, sum(price) as total FROM finance_app_stuff GROUP BY title ORDER BY total ASC')
    body = []
    for i in stuff:
        body.append(dict(title=i.title, total=i.total))
    headers = ['title', 'total']
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/stuff_group_title.html', context)


# sorting the food
def items_list_group_title(request):
    food_products = FoodProducts.objects.raw('SELECT id, title, sum(amount) as amount,'
                                             'sum(amount*price) as total'
                                             'FROM finance_app_foodproducts GROUP BY title')
    headers = ['title', 'amount', 'total']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list_group.html', context)


def food_order_price_asc(request):
    food_products = FoodProducts.objects.raw('SELECT id, title, SUM(amount) as amount,'
                                             ' date, SUM(amount*price) as total'
                                             ' FROM finance_app_foodproducts GROUP BY title ORDER BY price')
    headers = ['title', 'amount', 'total', 'date']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list_group.html', context)


def food_order_price_desc(request):
    food_products = FoodProducts.objects.raw('SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts GROUP BY title ORDER BY price DESC')
    headers = ['title', 'amount', 'price', 'total', 'date']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list.html', context)


def food_order_title_asc(request):
    food_products = FoodProducts.objects.raw(
        'SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts ORDER BY title')
    headers = ['title', 'amount', 'price', 'total', 'date']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list.html', context)


def food_order_title_desc(request):
    food_products = FoodProducts.objects.raw(
        'SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts GROUP BY title ORDER BY title DESC')
    headers = ['title', 'amount', 'price', 'total', 'date']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list.html', context)


def food_order_amount_asc(request):
    food_products = FoodProducts.objects.raw(
        'SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts GROUP BY title ORDER BY amount')
    headers = ['title', 'amount', 'price', 'total', 'date']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list.html', context)


def food_order_amount_desc(request):
    food_products = FoodProducts.objects.raw(
        'SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts GROUP BY title ORDER BY amount DESC')
    headers = ['title', 'amount', 'price', 'total', 'date']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list.html', context)


def food_order_total_asc(request):
    food_products = FoodProducts.objects.raw(
        'SELECT id, title, SUM(amount) as amount, sum(price) as price, date, sum(amount*price) as total FROM finance_app_foodproducts GROUP BY title ORDER BY total')
    headers = ['title', 'amount', 'price', 'total', 'date']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list.html', context)


def food_order_total_desc(request):
    food_products = FoodProducts.objects.raw(
        'SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts GROUP BY title ORDER BY total DESC')
    headers = ['title', 'amount', 'price', 'total', 'date']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list.html', context)


def food_order_date_asc(request):
    food_products = FoodProducts.objects.raw(
        'SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts GROUP BY title ORDER BY price')
    headers = ['title', 'amount', 'price', 'total', 'date']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list.html', context)


def food_order_date_desc(request):
    food_products = FoodProducts.objects.raw(
        'SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts GROUP BY title ORDER BY price')
    headers = ['title', 'amount', 'price', 'total', 'date']
    body = []
    for food in food_products:
        body.append(dict(title=food.title, amount=food.amount,
                         price=food.price, total=food.total, date=str(food.date)[:10]))
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/items_list.html', context)


def test(request):
    headers = ['date', 'a', 'b', 'c']
    body = [{'date': '2015-10-16', 'a': 1, 'b': 2, 'c': 3},
            {'date': '2015-10-17', 'a': 4, 'b': 5, 'c': 6}]
    context = {'headers': headers, 'body': body}
    return render(request, 'finance_app/test.html', context)
