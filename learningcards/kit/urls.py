from django.urls import path

from . import views

app_name = "kit"
urlpatterns = [
    path("<str:kit_name>/", views.kit, name="kit"),
]