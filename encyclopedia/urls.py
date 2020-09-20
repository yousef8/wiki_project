from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<title>/" , views.view_entry , name="view_entry"),
    path("search/" , views.search , name="search_entry"),
    path("newpage/" , views.new_page , name="new_page"),
    path("editpage/<title>/" , views.edit_page , name="edit_page"),
    path("randompage/" , views.random_page , name="random_page")
]
