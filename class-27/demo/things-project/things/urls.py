from django.urls import path
from .views import HomeView, AboutView, ThingListView, ThingDetailView

urlpatterns = [
    path("home/", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("", ThingListView.as_view(), name="thing_list"),
    path("<int:pk>/", ThingDetailView.as_view(), name="thing_detail"),
]
