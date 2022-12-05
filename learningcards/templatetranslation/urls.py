from django.urls import path

from .views import GetTranslateTemplate

app_name = "templatetranslation"
urlpatterns = [
    path("translation/<str:view_name>/", GetTranslateTemplate.as_view(), name="get_translate"),
]