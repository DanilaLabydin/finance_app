from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items_list/', views.items_list, name='items_list'),
    path('stuff_list', views.stuff_list, name='stuff_list'),
    path('items_list/new_item/', views.add_item, name='new_item'),
    path('new_stuff/', views.add_stuff, name='new_stuff'),
    path('test/', views.test, name='test'),
    path('stuff_price_asc', views.stuff_order_price_asc, name='stuff_price_asc'),
    path('stuff_price_desc', views.stuff_order_price_desc, name='stuff_price_desc'),
    path('stuff_title_asc', views.stuff_order_title_asc, name='stuff_title_asc'),
    path('stuff_title_desc', views.stuff_order_title_desc, name='stuff_title_desc'),
    path('stuff_date_asc', views.stuff_order_date_asc, name='stuff_date_asc'),
    path('stuff_date_desc', views.stuff_order_date_desc, name='stuff_date_desc'),
]
