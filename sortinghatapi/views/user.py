from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.db import models
from sortinghatapi.serializers import UserSerializer
from sortinghatapi.models import User

class UserView(ViewSet):
   
   def retrieve(self, request, pk):
       
       user= User.objects.get(pk=pk)
       serializer = UserSerializer(user)
       data =serializer.data
       
       return Response(data)
     
     
   def list(self,request):
        
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

   def create(self, request):
    
    user = User(
      first_name=request.data["firstName"],
      last_name=request.data["lastName"],
      email=request.data["email"]
    )
    user.save()
    serializer = UserSerializer(user)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

   def update(self, request, pk):
        user = User.objects.get(pk=pk)
        user.first_name = request.data.get("firstName", user.first_name)
        user.last_name = request.data.get("lastName", user.last_name)
        user.email = request.data.get("email", user.email)
        
        user.save()
        
        serializer = UserSerializer(user)
        return Response(serializer.data)

   def destroy(self, request, pk):
        user = User.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
