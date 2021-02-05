from django.urls import path
from . import views


app_name = "api"
urlpatterns = [
    path('', views.Home.as_view(), name="Home")
]
