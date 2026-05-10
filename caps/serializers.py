

from rest_framework.relations import StringRelatedField

from caps.models import Caps
from rest_framework import serializers

class CapsSerializer(serializers.ModelSerializer):
    
    
    brand_name = serializers.ReadOnlyField(source='brand.name')
    
    class Meta:
        model = Caps
        fields =  ('url', 'id','name', 'description', 'price', 'image', 'stock', 'brand', 'brand_name')
    def create(self, validated_data):
        cap = Caps.objects.create(**validated_data)
        return cap