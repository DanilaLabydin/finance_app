from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("items_list/", views.items_list, name="items_list"),
    path("stuff_list", views.stuff_list, name="stuff_list"),
    path("items_list/new_item/", views.add_item, name="new_item"),
    path("new_stuff/", views.add_stuff, name="new_stuff"),
    path("sstuff_months/", views.sstuff_months, name="sstuff_months"),
    path("ffood_months/", views.ffood_months, name="ffood_months"),
    # group by title stuff
    path(
        "stuff_list_group_title_asc",
        views.stuff_group_title_asc,
        name="stuff_list_group_title_asc",
    ),
    path(
        "stuff_list_group_title_desc",
        views.stuff_group_title_desc,
        name="stuff_list_group_title_desc",
    ),
    path(
        "stuff_list_group_title_total_asc",
        views.stuff_group_title_total_asc,
        name="stuff_list_group_title_total_asc",
    ),
    path(
        "stuff_list_group_title_total_desc",
        views.stuff_group_title_total_desc,
        name="stuff_list_group_title_total_desc",
    ),
    # group by date stuff
    path(
        "stuff_list_group_date_total_desc",
        views.stuff_group_date_total_desc,
        name="stuff_list_group_date_total_desc",
    ),
    path(
        "stuff_list_group_date_total_asc",
        views.stuff_group_date_total_asc,
        name="stuff_list_group_date_total_asc",
    ),
    path(
        "stuff_list_group_date_date_desc",
        views.stuff_group_date_date_desc,
        name="stuff_list_group_date_date_desc",
    ),
    path(
        "stuff_list_group_date_date_asc",
        views.stuff_group_date_date_asc,
        name="stuff_list_group_date_date_asc",
    ),
    # stuff sorting
    path("stuff_price_asc", views.stuff_order_price_asc, name="stuff_price_asc"),
    path("stuff_price_desc", views.stuff_order_price_desc, name="stuff_price_desc"),
    path("stuff_title_asc", views.stuff_order_title_asc, name="stuff_title_asc"),
    path("stuff_title_desc", views.stuff_order_title_desc, name="stuff_title_desc"),
    path("stuff_date_asc", views.stuff_order_date_asc, name="stuff_date_asc"),
    path("stuff_date_desc", views.stuff_order_date_desc, name="stuff_date_desc"),
    # group by title food
    path(
        "items_list_group_title_desc",
        views.items_list_group_title_desc,
        name="items_list_group_title_desc",
    ),
    path(
        "items_list_group_title",
        views.items_list_group_title,
        name="items_list_group_title",
    ),
    path(
        "items_list_group_title_amount_desc",
        views.items_list_group_title_amount_desc,
        name="items_list_group_title_amount_desc",
    ),
    path(
        "items_list_group_title_amount_asc",
        views.items_list_group_title_amount_asc,
        name="items_list_group_title_amount_asc",
    ),
    path(
        "items_list_group_title_total_desc",
        views.items_list_group_title_total_desc,
        name="items_list_group_title_total_desc",
    ),
    path(
        "items_list_group_title_total_asc",
        views.items_list_group_title_total_asc,
        name="items_list_group_title_total_asc",
    ),
    # group by date food
    path(
        "items_list_group_date_total_asc",
        views.items_list_group_date_total_asc,
        name="items_list_group_date_total_asc",
    ),
    path(
        "items_list_group_date_total_desc",
        views.items_list_group_date_total_desc,
        name="items_list_group_date_total_desc",
    ),
    path(
        "items_list_group_date_amount_asc",
        views.items_list_group_date_amount_asc,
        name="items_list_group_date_amount_asc",
    ),
    path(
        "items_list_group_date_amount_desc",
        views.items_list_group_date_amount_desc,
        name="items_list_group_date_amount_desc",
    ),
    path(
        "items_list_group_date_asc",
        views.items_list_group_date_amount_asc,
        name="items_list_group_date_asc",
    ),
    path(
        "items_list_group_date_desc",
        views.items_list_group_date_amount_desc,
        name="items_list_group_date_desc",
    ),
    # food sorting
    path("food_price_asc", views.food_order_price_asc, name="food_price_asc"),
    path("food_price_desc", views.food_order_price_desc, name="food_price_desc"),
    path("food_title_asc", views.food_order_title_asc, name="food_title_asc"),
    path("food_title_desc", views.food_order_title_desc, name="food_title_desc"),
    path("food_amount_asc", views.food_order_amount_asc, name="food_amount_asc"),
    path("food_amount_desc", views.food_order_amount_desc, name="food_amount_desc"),
    path("food_total_asc", views.food_order_total_asc, name="food_total_asc"),
    path("food_total_desc", views.food_order_total_desc, name="food_total_desc"),
    path("food_date_asc", views.food_order_date_asc, name="food_date_asc"),
    path("food_date_desc", views.food_order_date_desc, name="food_date_desc"),
    # ffood july
    path("ffood_months/ffood_list", views.ffood_list_july, name="ffood_list"),
    path("ffood_months/new_ffood", views.new_ffood, name="new_ffood"),
    # sstuff july
    path("sstuff_months/sstuff_list", views.sstuff_list_july, name="sstuff_list"),
    path("sstuff_months/new_sstuff/", views.add_sstuff, name="new_sstuff"),
    path(
        "sstuff_title_desc",
        views.sstuff_order_title_desc_july,
        name="sstuff_title_desc",
    ),
    path(
        "sstuff_title_asc", views.sstuff_order_title_asc_july, name="sstuff_title_asc"
    ),
    path(
        "sstuff_price_asc", views.sstuff_order_price_asc_july, name="sstuff_price_asc"
    ),
    path(
        "sstuff_price_desc",
        views.sstuff_order_price_desc_july,
        name="sstuff_price_desc",
    ),
    path("sstuff_date_asc", views.sstuff_order_date_asc_july, name="sstuff_date_asc"),
    path(
        "sstuff_date_desc", views.sstuff_order_date_desc_july, name="sstuff_date_desc"
    ),
]
