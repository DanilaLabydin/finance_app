from django.shortcuts import render
from django.http import HttpResponse
from .models import FoodProducts
from django.views.generic import CreateView
from .forms import FoodProductsForm


def index(request):
    food_products = FoodProducts.objects.all()
    context = {'food_products': food_products}
    return render(request, 'finance_app/index.html', context)


class ListCreate(CreateView):
    template_name = 'add_item_form.html'
    model = FoodProducts
    fields = ['title', 'amount', 'price', 'date']

    def get_context_data(self, **kwargs):
        context = super(ListCreate, self).get_context_data()
        context['title'] = 'Add a new list'
        return context


def add_item(request):
    if request.method != 'POST':
        form = FoodProductsForm()
    else:
        form = FoodProductsForm(data=request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'finance_app/add_item_form.html', context)