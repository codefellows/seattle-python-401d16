from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Sweet
from .permissions import IsPurchaserOrReadOnly
from .serializers import SweetSerializer


class SweetList(ListCreateAPIView):
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer


class SweetDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsPurchaserOrReadOnly,)
    queryset = Sweet.objects.all()
    serializer_class = SweetSerializer
