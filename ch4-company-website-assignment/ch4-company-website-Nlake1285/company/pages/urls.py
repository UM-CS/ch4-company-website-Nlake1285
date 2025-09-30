# pages/urls.py
from django.urls import path

from .views import AboutPageView, ProductPageView, home_page_view

urlpatterns = [
    path("about/", AboutPageView.as_view(), name = "about"),  # new
    path("", home_page_view, name = "home"),
    path("products/", ProductPageView.as_view(), name = "products"),  # new
]