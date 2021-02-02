from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:title>", views.get_entry, name="get_entry"),
    path("search_result/", views.search_result, name="search_result")
]
