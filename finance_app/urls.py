from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('items_list/', views.items_list, name='items_list'),
    path('rests_list', views.rests_list, name='rests_list'),
    path('new_item/', views.add_item, name='new_item'),
    path('new_rest/', views.add_rest, name='new_rest'),
]
