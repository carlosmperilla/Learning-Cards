from django.urls import path

from . import views

app_name = "card"
urlpatterns = [
    path("show-native-word/<str:kit_name>", views.show_native_word, name="show_native_word"),
    path("replace-img/<str:kit_name>", views.replace_img, name="replace_img"),
    path("check-answer/<str:kit_name>", views.check_answer, name="check_answer"),
]