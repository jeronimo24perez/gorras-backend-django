
from brands.models import Brand
from rest_framework import serializers


class BrandSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Brand
        fields = ['url', 'id', 'name', 'img']
    def create(self, validated_data):
        return Brand.objects.create(**validated_data)