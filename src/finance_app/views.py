import datetime

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import FoodProducts, Rest, Stuff, SStuff, FFoodProducts, Category, Spent
from django.views.generic import CreateView
from .forms import FoodProductsForm, StuffForm, SStuffForm, FFoodForm, CategoryForm


def index(request):
    return render(request, "finance_app/index.html")


def get_all_user_spents(request):
    ...


def get_user_category(request):
    try:
        categories = Category.objects.all()
    except Exception as e:
        return 
    headers = ["id", "name", "description"]
    body = [dict(id=cat_obj.id, name=cat_obj.name, description=cat_obj.description) for cat_obj in categories]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/categories.html", context)


def add_item(request):
    if request.method != "POST":
        form = FoodProductsForm()
    else:
        form = FoodProductsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("items_list")

    context = {"form": form}
    return render(request, "finance_app/add_item.html", context)


def add_user_category(request):
    if request.method != "POST":
        form = CategoryForm()
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_all_categories")
    context = {"form": form}
    return render(request, "finance_app/add_category.html", context)


def sstuff_months(request):
    return render(request, "finance_app/sstuff_months.html")


def ffood_months(request):
    return render(request, "finance_app/ffood_months.html")


def items_list(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts"
    )
    headers = ["title", "amount", "price", "total", "date"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                price=food.price,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list.html", context)


def stuff_list(request):
    stuff = Stuff.objects.all()
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ["title", "price", "date"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_list.html", context)


def add_item(request):
    if request.method != "POST":
        form = FoodProductsForm()
    else:
        form = FoodProductsForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("items_list")

    context = {"form": form}
    return render(request, "finance_app/add_item.html", context)


def add_stuff(request):
    if request.method != "POST":
        form = StuffForm
    else:
        form = StuffForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("stuff_list")

    context = {"form": form}
    return render(request, "finance_app/add_stuff.html", context)


# sorting the stuff
def stuff_order_price_asc(request):
    stuff = Stuff.objects.order_by("price")
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ["title", "price", "date"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_list.html", context)


def stuff_order_price_desc(request):
    stuff = Stuff.objects.order_by("-price")
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ["title", "price", "date"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_list.html", context)


def stuff_order_title_asc(request):
    stuff = Stuff.objects.order_by("title")
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ["title", "price", "date"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_list.html", context)


def stuff_order_title_desc(request):
    stuff = Stuff.objects.order_by("-title")
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ["title", "price", "date"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_list.html", context)


def stuff_order_date_asc(request):
    stuff = Stuff.objects.order_by("date")
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ["title", "price", "date"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_list.html", context)


def stuff_order_date_desc(request):
    stuff = Stuff.objects.order_by("-date")
    body = []
    for i in stuff:
        body.append(dict(title=i.title, price=i.price, date=str(i.date)[:10]))
    headers = ["title", "price", "date"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_list.html", context)


# stuff group by title
def stuff_group_title_asc(request):
    stuff = Stuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_stuff GROUP BY title ORDER BY title"
    )
    body = []
    for i in stuff:
        body.append(dict(title=i.title, total=i.total))
    headers = ["title", "total"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_group_title.html", context)


def stuff_group_title_desc(request):
    stuff = Stuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_stuff GROUP BY title ORDER BY title DESC"
    )
    body = []
    for i in stuff:
        body.append(dict(title=i.title, total=i.total))
    headers = ["title", "total"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_group_title.html", context)


def stuff_group_title_total_desc(request):
    stuff = Stuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_stuff GROUP BY title ORDER BY total DESC"
    )
    body = []
    for i in stuff:
        body.append(dict(title=i.title, total=i.total))
    headers = ["title", "total"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_group_title.html", context)


def stuff_group_title_total_asc(request):
    stuff = Stuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_stuff GROUP BY title ORDER BY total ASC"
    )
    body = []
    for i in stuff:
        body.append(dict(title=i.title, total=i.total))
    headers = ["title", "total"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_group_title.html", context)


# stuff group by date
def stuff_group_date_total_desc(request):
    stuff = Stuff.objects.raw(
        "SELECT id, date, sum(price) as total FROM finance_app_stuff GROUP BY date ORDER BY total DESC"
    )
    body = []
    for i in stuff:
        body.append(dict(date=str(i.date)[:10], total=i.total))
    headers = ["total", "date"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_group_date.html", context)


def stuff_group_date_total_asc(request):
    stuff = Stuff.objects.raw(
        "SELECT id, date, sum(price) as total FROM finance_app_stuff GROUP BY date ORDER BY total"
    )
    body = []
    for i in stuff:
        body.append(dict(date=str(i.date)[:10], total=i.total))
    headers = ["total", "date"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_group_date.html", context)


def stuff_group_date_date_desc(request):
    stuff = Stuff.objects.raw(
        "SELECT id, date, sum(price) as total FROM finance_app_stuff GROUP BY date ORDER BY date DESC"
    )
    body = []
    for i in stuff:
        body.append(dict(date=str(i.date)[:10], total=i.total))
    headers = ["total", "date"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_group_date.html", context)


def stuff_group_date_date_asc(request):
    stuff = Stuff.objects.raw(
        "SELECT id, date, sum(price) as total FROM finance_app_stuff GROUP BY date ORDER BY date"
    )
    body = []
    for i in stuff:
        body.append(dict(date=str(i.date)[:10], total=i.total))
    headers = ["total", "date"]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/stuff_group_date.html", context)


# sorting the food
# food group by title
def items_list_group_title(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, sum(amount) as amount,"
        "sum(amount*price) as total "
        "FROM finance_app_foodproducts GROUP BY title ORDER BY title"
    )
    headers = ["title", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group.html", context)


def items_list_group_title_desc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, sum(amount) as amount,"
        "sum(amount*price) as total "
        "FROM finance_app_foodproducts GROUP BY title ORDER BY title DESC"
    )
    headers = ["title", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group.html", context)


def items_list_group_title_amount_asc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, sum(amount) as amount,"
        "sum(amount*price) as total "
        "FROM finance_app_foodproducts GROUP BY title ORDER BY amount ASC"
    )
    headers = ["title", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group.html", context)


def items_list_group_title_amount_desc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, sum(amount) as amount,"
        "sum(amount*price) as total "
        "FROM finance_app_foodproducts GROUP BY title ORDER BY amount DESC"
    )
    headers = ["title", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group.html", context)


def items_list_group_title_total_asc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, sum(amount) as amount,"
        "sum(amount*price) as total "
        "FROM finance_app_foodproducts GROUP BY title ORDER BY total ASC"
    )
    headers = ["title", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group.html", context)


def items_list_group_title_total_desc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, sum(amount) as amount,"
        "sum(amount*price) as total "
        "FROM finance_app_foodproducts GROUP BY title ORDER BY total DESC"
    )
    headers = ["title", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group.html", context)


# group by date food
def items_list_group_date_total_asc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, sum(amount) as amount,"
        "sum(amount*price) as total, date "
        "FROM finance_app_foodproducts GROUP BY date ORDER BY total ASC"
    )
    headers = ["date", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group_date.html", context)


def items_list_group_date_total_desc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, sum(amount) as amount,"
        "sum(amount*price) as total, date "
        "FROM finance_app_foodproducts GROUP BY date ORDER BY total DESC"
    )
    headers = ["date", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group_date.html", context)


def items_list_group_date_amount_asc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, sum(amount) as amount,"
        "sum(amount*price) as total, date "
        "FROM finance_app_foodproducts GROUP BY date ORDER BY amount ASC"
    )
    headers = ["date", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group_date.html", context)


def items_list_group_date_amount_desc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, sum(amount) as amount,"
        "sum(amount*price) as total, date "
        "FROM finance_app_foodproducts GROUP BY date ORDER BY amount DESC"
    )
    headers = ["date", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group_date.html", context)


def items_list_group_date_asc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, sum(amount) as amount,"
        "sum(amount*price) as total, date "
        "FROM finance_app_foodproducts GROUP BY date ORDER BY date ASC"
    )
    headers = ["date", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group_date.html", context)


def items_list_group_date_desc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, sum(amount) as amount,"
        "sum(amount*price) as total, date "
        "FROM finance_app_foodproducts GROUP BY date ORDER BY date DESC"
    )
    headers = ["date", "amount", "total"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list_group_date.html", context)


# sorting food


def food_order_price_asc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts ORDER BY price asc"
    )
    headers = ["title", "amount", "price", "total", "date"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                price=food.price,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list.html", context)


def food_order_price_desc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts ORDER BY price DESC"
    )
    headers = ["title", "amount", "price", "total", "date"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                price=food.price,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list.html", context)


def food_order_title_asc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts ORDER BY title"
    )
    headers = ["title", "amount", "price", "total", "date"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                price=food.price,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list.html", context)


def food_order_title_desc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts title ORDER BY title DESC"
    )
    headers = ["title", "amount", "price", "total", "date"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                price=food.price,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list.html", context)


def food_order_amount_asc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts title ORDER BY amount"
    )
    headers = ["title", "amount", "price", "total", "date"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                price=food.price,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list.html", context)


def food_order_amount_desc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts ORDER BY amount DESC"
    )
    headers = ["title", "amount", "price", "total", "date"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                price=food.price,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list.html", context)


def food_order_total_asc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts ORDER BY total"
    )
    headers = ["title", "amount", "price", "total", "date"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                price=food.price,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list.html", context)


def food_order_total_desc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts ORDER BY total DESC"
    )
    headers = ["title", "amount", "price", "total", "date"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                price=food.price,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list.html", context)


def food_order_date_asc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts  ORDER BY price"
    )
    headers = ["title", "amount", "price", "total", "date"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                price=food.price,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list.html", context)


def food_order_date_desc(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts ORDER BY price DESC"
    )
    headers = ["title", "amount", "price", "total", "date"]
    body = []
    for food in food_products:
        body.append(
            dict(
                title=food.title,
                amount=food.amount,
                price=food.price,
                total=food.total,
                date=str(food.date)[:10],
            )
        )
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/items_list.html", context)


def test(request):
    headers = ["date", "a", "b", "c"]
    body = [
        {"date": "2015-10-16", "a": 1, "b": 2, "c": 3},
        {"date": "2015-10-17", "a": 4, "b": 5, "c": 6},
    ]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/test.html", context)


def test_template(request):
    food_products = FoodProducts.objects.raw(
        "SELECT id, title, amount, price, date, amount*price as total FROM finance_app_foodproducts"
    )
    context = {"food_products": food_products}
    return render(request, "finance_app/test2.html", context)


# SSTUFF July
def sstuff_list_july(request):
    stuff = SStuff.objects.all()
    body = []
    for i in stuff:
        body.append(
            dict(title=i.title, price=i.price, date=str(i.date)[:10], month=i.month)
        )
    headers = ["title", "price", "date", "month"]
    # the biggest price table
    stuff_biggest_price = SStuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_sstuff GROUP BY title ORDER BY total DESC LIMIT 5"
    )
    body_big_price = []
    for i in stuff_biggest_price:
        body_big_price.append(dict(title=i.title, total=i.total))
    headers_big_price = ["title", "total"]

    # total
    total_sum = SStuff.objects.raw(
        "SELECT id, sum(price) as total FROM finance_app_sstuff"
    )

    context = {
        "headers": headers,
        "body": body,
        "headers_big_price": headers_big_price,
        "body_big_price": body_big_price,
        "total_sum": total_sum,
    }
    return render(request, "finance_app/sstuff_list_july.html", context)


def add_sstuff(request):
    if request.method != "POST":
        form = SStuffForm
    else:
        form = SStuffForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("sstuff_list")

    context = {"form": form}
    return render(request, "finance_app/add_sstuff.html", context)


def sstuff_order_title_asc_july(request):
    stuff = SStuff.objects.order_by("title")
    body = []
    for i in stuff:
        body.append(
            dict(title=i.title, price=i.price, date=str(i.date)[:10], month=i.month)
        )
    headers = ["title", "price", "date", "month"]
    # the biggest price table
    stuff_biggest_price = SStuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_sstuff GROUP BY title ORDER BY total DESC LIMIT 5"
    )
    body_big_price = []
    for i in stuff_biggest_price:
        body_big_price.append(dict(title=i.title, total=i.total))
    headers_big_price = ["title", "total"]

    context = {
        "headers": headers,
        "body": body,
        "headers_big_price": headers_big_price,
        "body_big_price": body_big_price,
    }
    return render(request, "finance_app/sstuff_list_july.html", context)


def sstuff_order_title_desc_july(request):
    stuff = SStuff.objects.order_by("-title")
    body = []
    for i in stuff:
        body.append(
            dict(title=i.title, price=i.price, date=str(i.date)[:10], month=i.month)
        )
    headers = ["title", "price", "date", "month"]
    # the biggest price table
    stuff_biggest_price = SStuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_sstuff GROUP BY title ORDER BY total DESC LIMIT 5"
    )
    body_big_price = []
    for i in stuff_biggest_price:
        body_big_price.append(dict(title=i.title, total=i.total))
    headers_big_price = ["title", "total"]

    context = {
        "headers": headers,
        "body": body,
        "headers_big_price": headers_big_price,
        "body_big_price": body_big_price,
    }
    return render(request, "finance_app/sstuff_list_july.html", context)


def sstuff_order_price_asc_july(request):
    stuff = SStuff.objects.order_by("price")
    body = []
    for i in stuff:
        body.append(
            dict(title=i.title, price=i.price, date=str(i.date)[:10], month=i.month)
        )
    headers = ["title", "price", "date", "month"]
    # the biggest price table
    stuff_biggest_price = SStuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_sstuff GROUP BY title ORDER BY total DESC LIMIT 5"
    )
    body_big_price = []
    for i in stuff_biggest_price:
        body_big_price.append(dict(title=i.title, total=i.total))
    headers_big_price = ["title", "total"]

    context = {
        "headers": headers,
        "body": body,
        "headers_big_price": headers_big_price,
        "body_big_price": body_big_price,
    }
    return render(request, "finance_app/sstuff_list_july.html", context)


def sstuff_order_price_desc_july(request):
    stuff = SStuff.objects.order_by("-price")
    body = []
    for i in stuff:
        body.append(
            dict(title=i.title, price=i.price, date=str(i.date)[:10], month=i.month)
        )
    headers = ["title", "price", "date", "month"]
    # the biggest price table
    stuff_biggest_price = SStuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_sstuff GROUP BY title ORDER BY total DESC LIMIT 5"
    )
    body_big_price = []
    for i in stuff_biggest_price:
        body_big_price.append(dict(title=i.title, total=i.total))
    headers_big_price = ["title", "total"]

    context = {
        "headers": headers,
        "body": body,
        "headers_big_price": headers_big_price,
        "body_big_price": body_big_price,
    }
    return render(request, "finance_app/sstuff_list_july.html", context)


def sstuff_order_date_asc_july(request):
    stuff = SStuff.objects.order_by("date")
    body = []
    for i in stuff:
        body.append(
            dict(title=i.title, price=i.price, date=str(i.date)[:10], month=i.month)
        )
    headers = ["title", "price", "date", "month"]
    # the biggest price table
    stuff_biggest_price = SStuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_sstuff GROUP BY title ORDER BY total DESC LIMIT 5"
    )
    body_big_price = []
    for i in stuff_biggest_price:
        body_big_price.append(dict(title=i.title, total=i.total))
    headers_big_price = ["title", "total"]

    context = {
        "headers": headers,
        "body": body,
        "headers_big_price": headers_big_price,
        "body_big_price": body_big_price,
    }
    return render(request, "finance_app/sstuff_list_july.html", context)


def sstuff_order_date_desc_july(request):
    # all data table
    stuff = SStuff.objects.order_by("-date")
    body = []
    for i in stuff:
        body.append(
            dict(title=i.title, price=i.price, date=str(i.date)[:10], month=i.month)
        )
    headers = ["title", "price", "date", "month"]

    # the biggest price table
    stuff_biggest_price = SStuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_sstuff GROUP BY title ORDER BY total DESC LIMIT 5"
    )
    body_big_price = []
    for i in stuff_biggest_price:
        body_big_price.append(dict(title=i.title, total=i.total))
    headers_big_price = ["title", "total"]

    context = {
        "headers": headers,
        "body": body,
        "headers_big_price": headers_big_price,
        "body_big_price": body_big_price,
    }
    return render(request, "finance_app/sstuff_list_july.html", context)


# FFOOD July
def ffood_list_july(request):
    stuff = FFoodProducts.objects.all()
    body = []
    for i in stuff:
        body.append(
            dict(title=i.title, price=i.price, date=str(i.date)[:10], month=i.month)
        )
    headers = ["title", "price", "date", "month"]
    # the biggest price table
    stuff_biggest_price = SStuff.objects.raw(
        "SELECT id, title, sum(price) as total FROM finance_app_sstuff GROUP BY title ORDER BY total DESC LIMIT 5"
    )
    body_big_price = []
    for i in stuff_biggest_price:
        body_big_price.append(dict(title=i.title, total=i.total))
    headers_big_price = ["title", "total"]

    # total
    total_sum = FFoodProducts.objects.raw(
        "SELECT id, sum(price) as total FROM finance_app_ffoodproducts"
    )

    context = {
        "headers": headers,
        "body": body,
        "headers_big_price": headers_big_price,
        "body_big_price": body_big_price,
        "total_sum": total_sum,
    }
    return render(request, "finance_app/ffood_list_july.html", context)


def new_ffood(request):
    if request.method != "POST":
        form = FFoodForm
    else:
        form = FFoodForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("ffood_list")

    context = {"form": form}
    return render(request, "finance_app/add_ffood.html", context)
