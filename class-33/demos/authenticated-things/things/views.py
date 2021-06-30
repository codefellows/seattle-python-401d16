from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import ThingSerializer
from .models import Thing
from .permissions import IsRaterOrReadOnly


class ThingList(ListCreateAPIView):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer


class ThingDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsRaterOrReadOnly,)
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer
