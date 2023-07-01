from django.db import models
from .user import User
from .house import House

class Student(models.Model):
  
  user = models.ForeignKey(User,on_delete=models.CASCADE, related_name='user',default=1 )
  house = models.ForeignKey(House, on_delete=models.CASCADE, related_name='house', default=1)

  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  image_url = models.CharField(max_length=300)
