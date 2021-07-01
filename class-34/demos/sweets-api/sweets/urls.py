from django.urls import path
from .views import SweetList, SweetDetail

urlpatterns = [
    path("", SweetList.as_view(), name="sweet_list"),
    path("<int:pk>/", SweetDetail.as_view(), name="sweet_detail"),
]
