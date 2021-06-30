from .views import ThingList, ThingDetail
from django.urls import path

urlpatterns = [
    path("", ThingList.as_view(), name="thing_list"),
    path("<int:pk>/", ThingDetail.as_view(), name="thing_detail"),
]
