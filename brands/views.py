from django.shortcuts import render
from rest_framework.permissions import AllowAny, IsAdminUser

from brands.models import Brand
from brands.serializers import BrandSerializer
from rest_framework import viewsets, mixins
# Create your views here.

class BrandsViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAdminUser()]
        return [AllowAny()]
