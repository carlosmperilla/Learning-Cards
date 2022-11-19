from django.urls import path

from . import views

app_name = "templatetranslation"
urlpatterns = [
    path("translation/<str:view_name>/", views.get_translate_template, name="get_translate"),
]