from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # /drone_order
]
