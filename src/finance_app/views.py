from django.shortcuts import (
    get_object_or_404, render, HttpResponseRedirect, redirect
    )
from django.http import Http404
from django.db.models import Sum

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
    body = [
        dict(id=cat_obj.id, name=cat_obj.name, description=cat_obj.description)
        for cat_obj in categories
    ]
    context = {"headers": headers, "body": body}
    return render(request, "finance_app/categories.html", context)


def get_user_spents(request):
    try:
        spents = Spent.objects.all()
        total_spent = Spent.objects.aggregate(total=Sum('price', default=0))
        category_spent = Spent.objects.raw('''
        SELECT c.id, c.name AS name, SUM(s.price) as price FROM finance_app_spent s LEFT JOIN finance_app_category c ON s.category_id = c.id GROUP BY c.id;''')
        cat_spents = []
        for i in category_spent:
            print(i)
            cat_spents.append(dict(name=i.name, price=i.price))
    except Exception as e:
        print(f'Error: {e}')
        return
    headers = ["id", "name", "price", "description", "category"]
    body = [
        dict(
            id=spent_obj.id,
            name=spent_obj.name,
            price=spent_obj.price,
            description=spent_obj.description,
            category=spent_obj.category,
            time_create=spent_obj.time_create,
            time_update=spent_obj.time_update,
        )
        for spent_obj in spents
    ]
    context = {
        "headers": headers,
        "body": body,
        "total_spent": total_spent,
        "category_spent": cat_spents
        }
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


def get_user_spent_by_id(request, spent_id):
    try:
        spent = Spent.objects.get(pk=spent_id)
        context = {"spent": spent, "spent_id": spent_id}
    except Spent.DoesNotExist:
        raise Http404("Spent with that id doesn't exist")
    return render(request, "finance_app/get_spent.html", context)


def get_user_category_by_id(request, category_id):
    try:
        category = Category.objects.get(pk=category_id)
        context = {"category": category, "category_id": category_id}
    except Category.DoesNotExist:
        raise Http404("Category with that id doesn't exist")
    return render(request, "finance_app/get_category.html", context)


def update_user_spent(request, spent_id):
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Spent, id=spent_id)

    # pass the object as instance in form
    form = SpentForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/spents")

    # add form dictionary to context
    context["form"] = form
    context["spent_id"] = spent_id

    return render(request, "finance_app/update_spent.html", context)


def update_user_category(request, category_id):
    context = {}

    obj = get_object_or_404(Category, id=category_id)
    form = CategoryForm(request.POST or None, instance=obj)

    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/categories")

    context["form"] = form
    context["category_id"] = category_id
    return render(request, "finance_app/update_category.html", context)


def delete_user_category(request, category_id):
    context = {}
    obj = get_object_or_404(Category, id=category_id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/categories")

    return render(request, "finance_app/delete_category.html", context)


def delete_user_spent(request, spent_id):
    context = {}
    obj = get_object_or_404(Spent, id=spent_id)

    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/spents")

    return render(request, "finance_app/delete_spent.html", context)
