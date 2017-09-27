from django.shortcuts import render
from rest_framework import viewsets
from .models import UserGroup, BasicProfile
from .serializers import UserSerializer,UserGroupSerializer
from rest_framework.renderers import TemplateHTMLRenderer
# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    queryset = BasicProfile.objects.all()
    serializer_class = UserSerializer
    # render(request,context)
    # renderer_classes = [TemplateHTMLRenderer]
    # template_name = 'signup.html'

    # def post(self, request):
    #     queryset = BasicProfile.objects.all()
    #     return Response({'BasicProfile': queryset})

class UserGroupViewSet(viewsets.ModelViewSet):
    queryset = UserGroup.objects.all()
    serializer_class = UserGroupSerializer