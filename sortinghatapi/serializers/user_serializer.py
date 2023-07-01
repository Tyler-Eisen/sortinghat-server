from rest_framework import serializers
from sortinghatapi.models import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
      model = User
      depth = 1
      fields = (
        'id',
        'first_name',
        'last_name',
        'email',
        'created_on',
        'uid'
      )
