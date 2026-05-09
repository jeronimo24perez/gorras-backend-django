from django.shortcuts import render
from rest_framework import generics

from .serializers import CapsSerializer
from caps.models import Caps

# Create your views here.

class Caps_list(generics.ListCreateAPIView):
    queryset = Caps.objects.all()
    serializer_class = CapsSerializer
class Caps_detail(generics.RetrieveAPIView):
    queryset = Caps.objects.all()
    serializer_class = CapsSerializer
