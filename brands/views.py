from django.shortcuts import render

from brands.models import Brand
from brands.serializers import BrandSerializer
from rest_framework import viewsets, mixins
# Create your views here.

class BrandsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
