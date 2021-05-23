from django.urls import URLPattern, path
from navigation import views

urlpatterns = [
    path("", views.home, name="home"),
]