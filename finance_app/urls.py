from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items_list/', views.items_list, name='items_list'),
    path('stuff_list', views.stuff_list, name='stuff_list'),
    path('items_list/new_item/', views.add_item, name='new_item'),
    path('new_stuff/', views.add_stuff, name='new_stuff'),
    path('test/', views.test, name='test'),
]
