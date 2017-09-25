from django.shortcuts import render
from rest_framework import viewsets
from .models import UserGroup, BasicProfile
from .serializers import UserSerializer,UserGroupSerializer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = BasicProfile.objects.all()
    serializer_class = UserSerializer

class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer