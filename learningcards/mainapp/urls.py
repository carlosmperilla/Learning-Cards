from django.urls import path

from . import views
from kit.views import add_kit


urlpatterns = [
    path("", views.index, name="index"),
    path("add_kit/", add_kit, name="add_kit"),
]