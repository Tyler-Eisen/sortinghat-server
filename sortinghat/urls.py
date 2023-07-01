
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from sortinghatapi.views.user import UserView
from sortinghatapi.views.house import HouseView
from sortinghatapi.views.student import StudentView

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'users', UserView, 'user')
router.register(r'houses', HouseView, 'house')
router.register(r'students', StudentView, 'student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),

]
