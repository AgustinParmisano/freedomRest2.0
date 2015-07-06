from django.forms import widgets
from rest_framework import serializers
from freedom.models import Room
from django.contrib.auth.models import User

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Room
        fields = ('url', 'owner', 'name')
        
class UserSerializer(serializers.HyperlinkedModelSerializer):
    rooms = serializers.HyperlinkedRelatedField(many=True, view_name='room-detail', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'rooms')