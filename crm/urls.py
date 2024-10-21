from django.urls import path
from .views import *

urlpatterns = [
    path("", Register.as_view(), name="register"),
    path("login/", login.as_view(), name="login"),
    path("grabe/", grabe.as_view(), name="grabe"),
    path("home/", home.as_view(), name="home"),
    path("raspis/", raspisania.as_view(), name="raspisania"),
        path("profile/", profile.as_view(), name="profile"),
]
