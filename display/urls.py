from django.urls import path

from . import views
app_name = "display"
urlpatterns = [
    path("clubs/", views.IndexView.as_view(), name="index"),
    path("clubs/<int:pk>/", views.DetailView.as_view(), name="club"),
    path("", views.LoginView.as_view(), name="login")
]