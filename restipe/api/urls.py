from django.urls import path

from . import views

urlpatterns = [
    path("", views.root),
    path("<int:id>", views.single),
    path("search", views.search)
]