from django.urls import path

from . import views

app_name = "kit"
urlpatterns = [
    path("cards/<str:kit_name>/", views.kit, name="kit"),
    path("action/edit", views.edit_kits, name="edit_kits"),
    path("action/delete", views.delete_kits, name="delete_kits"),
]