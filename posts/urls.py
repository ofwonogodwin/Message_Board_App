from django.urls import path
from .views import homePage
urlpatterns = [
    path('',homePage.as_view(),name="homie"),
]