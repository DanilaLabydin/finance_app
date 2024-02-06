from django.shortcuts import render, redirect
from .models import Category, Spent
from .forms import CategoryForm, SpentForm


def index(request):
    return render(request, "finance_app/index.html")


def get_user_category(request):
    try:
        categories = Category.objects.all()
    except Exception as e:
        return 
    headers = ["id", "name", "description"]
    body = [dict(id=cat_obj.id, name=cat_obj.name, description=cat_obj.description) for cat_obj in categories]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/categories.html", context)


def get_user_spents(request):
    try:
        spents = Spent.objects.all()
    except Exception as e:
        return
    headers = ["id","name", "price", "description", "category"]
    body = [dict(id=spent_obj.id, name=spent_obj.name, price=spent_obj.price, description=spent_obj.description, category=spent_obj.category) for spent_obj in spents]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/spents.html", context)



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


def add_user_spent(request):
    if request.method != "POST":
        form = SpentForm()
    else:
        form = SpentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("get_all_spents")
    context = {"form": form}
    return render(request, "finance_app/add_spent.html", context)


def get_user_spent_by_id(request):
    pass


def get_user_category_by_id(request):
    pass


def update_user_spent(request):
    pass


def update_user_category(request):
    pass


def delete_user_category(request):
    pass


