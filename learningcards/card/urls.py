from django.urls import path

from .views import (
                   ShowNativeWord,
                   ReplaceImg,
                   CheckAnswer,
                   )

app_name = "card"
urlpatterns = [
    path("show-native-word/<str:kit_name>", ShowNativeWord.as_view(), name="show_native_word"),
    path("replace-img/<str:kit_name>", ReplaceImg.as_view(), name="replace_img"),
    path("check-answer/<str:kit_name>", CheckAnswer.as_view(), name="check_answer"),
]