from django.urls import path
from . import views

app_name = "core"
urlpatterns = [
    path("", views.home, name="home"),
    path("dashboard.png", views.dashboard_plot, name="dashboard_plot"),
]
