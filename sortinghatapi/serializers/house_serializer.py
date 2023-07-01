from rest_framework import serializers
from sortinghatapi.models import House

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ('id', 'name')
