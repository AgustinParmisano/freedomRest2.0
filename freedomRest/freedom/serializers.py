from django.forms import widgets
from rest_framework import serializers
from freedom.models import Room
from freedom.models import Sensor
from django.contrib.auth.models import User

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.username')
    sensors = serializers.HyperlinkedRelatedField(many=True, read_only=True,  view_name='sensor-detail')

    class Meta:
        model = Room
        fields = ('url', 'roomName', 'sensors')

class SensorSerializer(serializers.HyperlinkedModelSerializer):
    #room = serializers.HyperlinkedRelatedField(many=True, view_name='room-detail', read_only=True)"
    #room = serializers.ReadOnlyField(source='room.name')"
    #room = RoomSerializer(many=True)

    class Meta:
        model = Sensor
        fields = ('url', 'room', 'sensorName')
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    rooms = serializers.HyperlinkedRelatedField(many=True, view_name='room-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'rooms')