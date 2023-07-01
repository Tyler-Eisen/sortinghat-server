from rest_framework import serializers
from sortinghatapi.models import Student
from sortinghatapi.serializers.student_serializer import StudentSerializer

from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from sortinghatapi.serializers.student_serializer import StudentSerializer
from sortinghatapi.models.student import Student

class StudentView(ViewSet):
    def retrieve(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            serializer = StudentSerializer(student)
            return Response(serializer.data)
        except Student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def list(self, request):
        students = Student.objects.all()
        house = request.query_params.get('house', None)
        if house is not None:
          students = students.filter(house_id=house)
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)

    def create(self, request):
        student = Student(
         user_id=request.data["userId"],
         house_id=request.data["houseId"],
         first_name=request.data["firstName"],
         last_name=request.data["lastName"],
         image_url=request.data["imageUrl"]
    )
        student.save()
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def update(self, request, pk):
        student = Student.objects.get(pk=pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, pk):
        student = Student.objects.get(pk=pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
