from django.urls import path
from .views import (index, get_user_category, add_user_category,
                     get_user_spents, add_user_spent, get_user_spent_by_id,
                     get_user_category_by_id, update_user_spent)


urlpatterns = [
    path("", index, name="main_page"),
    path("categories/", get_user_category, name="get_all_categories"),
    path("spents/", get_user_spents, name="get_all_spents" ),
    path("categories/new_category", add_user_category, name="new_category"),
    path("spents/new_spent", add_user_spent, name="new_spent"),
    path("spents/<int:spent_id>", get_user_spent_by_id, name="get_spent"),
    path("categories/<int:category_id>", get_user_category_by_id, name="get_category"),
    path("spents/<int:spent_id>/update", update_user_spent, name="update_spent")

]
