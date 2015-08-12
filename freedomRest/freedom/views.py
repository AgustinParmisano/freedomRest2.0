from freedom.models import Room
from freedom.serializers import RoomSerializer
from freedom.models import Sensor
from freedom.serializers import SensorSerializer
from rest_framework import generics
from django.contrib.auth.models import User
from freedom.serializers import UserSerializer
from rest_framework import permissions
from freedom.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework import viewsets
from rest_framework.decorators import detail_route


@api_view(('GET',))
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'rooms': reverse('room-list', request=request, format=format),
        'sensors': reverse('sensor-list', request=request, format=format),
    })

class RoomViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    """def perform_create(self, serializer):
            serializer.save(owner=self.request.user)"""

class SensorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    """def perform_create(self, serializer):
            serializer.save(owner=self.request.user)"""

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer