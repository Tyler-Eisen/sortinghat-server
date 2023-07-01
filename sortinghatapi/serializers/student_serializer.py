from rest_framework import serializers
from sortinghatapi.models import Student

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Student
        fields = ('id', 'user', 'house', 'first_name', 'last_name', 'image_url')
