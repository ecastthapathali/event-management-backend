from django.urls import path
from . import views

urlpatterns = [
    path("",views.UserDataAPI.as_view(),name="user_data_api"),
    path("login/",views.UserLogin.as_view(),name="user_login"),
]
