from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.get_entry, name="get_entry"),
    path("search_result/", views.search_result, name="search_result"),
    path("new_page/", views.new_page, name="new_page"),
    path("edit_page/", views.edit_page, name="edit_page"),
    path("edit_entry/", views.edit_entry, name="edit_entry")
]
