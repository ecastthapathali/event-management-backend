from django.urls import path
from . import views

urlpatterns = [
    path("",views.UserDataListCreateAPI.as_view(),name="user_data_api"),
    path("<int:pk>/",views.UserDataRUDAPI.as_view(),name="user_data_api_each"),
    path("login/",views.UserLogin.as_view(),name="user_login"),
    path("events/",views.EventListCreateAPI.as_view(),name="event_api"),
    path("events/<int:pk>/",views.EventRUDAPI.as_view(),name="event_api_each"),
    path("reg/",views.EventRegAPI.as_view(),name="event_reg"),
    path("reg/<int:pk>/",views.EventRUDAPI.as_view(),name="event_reg_each"),
    path("participants/",views.ParticipantsAPI.as_view(),name="participants"),
    path("participants/<int:pk>/",views.ParticipantsRUDAPI.as_view(),name="participants_each"),
    path("digitalcert/",views.DigitalCertAPI.as_view(),name="digital_cert"),
    path("digitalcert/<int:pk>/",views.DigitalCertRUDAPI.as_view(),name="digital_cert_each"),
]
