from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from sortinghatapi.serializers.house_serializer import HouseSerializer
from sortinghatapi.models.house import House

class HouseView(ViewSet):
    def retrieve(self, request, pk):
        try:
            house = House.objects.get(pk=pk)
            serializer = HouseSerializer(house)
            return Response(serializer.data)
        except House.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        houses = House.objects.all()
        serializer = HouseSerializer(houses, many=True)
        return Response(serializer.data)

    def create(self, request):
        house = House(name=request.data["name"])
        house.save()
        serializer = HouseSerializer(house)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk):
        house = House.objects.get(pk=pk)
        house.name = request.data["name"]
        house.save()
        serializer = HouseSerializer(house)
        return Response(serializer.data)

    def destroy(self, request, pk):
        house = House.objects.get(pk=pk)
        house.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
