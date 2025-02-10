from django.urls import path
from .views import HomeView, AboutView, ActivitiesView

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("activities/", ActivitiesView.as_view(), name="activities"),
]
