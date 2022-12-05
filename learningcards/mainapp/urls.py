from django.urls import path

from .views import IndexPageView
from kit.views import add_kit


urlpatterns = [
    path("", IndexPageView.as_view(), name="index"),
    path("add_kit/", add_kit, name="add_kit"),
]