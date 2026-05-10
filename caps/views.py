from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAdminUser

from .serializers import CapsSerializer
from caps.models import Caps

# Create your views here.

class Caps_list(generics.ListAPIView):
    queryset = Caps.objects.all()
    serializer_class = CapsSerializer

class Caps_create(generics.CreateAPIView):
    queryset = Caps.objects.all()
    serializer_class = CapsSerializer

    permission_classes = [IsAdminUser]
class Caps_detail(generics.RetrieveAPIView):
    queryset = Caps.objects.all()
    serializer_class = CapsSerializer
