from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('new_item/', views.add_item, name='new_item'),
]
