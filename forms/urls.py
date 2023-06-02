from django.urls import path, include
from .views import *
urlpatterns = [
    path("", Index, name="index"),
    path("display", Display, name="display"),

]
