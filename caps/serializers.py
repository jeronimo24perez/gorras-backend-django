

from caps.models import Caps
from rest_framework import serializers

class CapsSerializer(serializers.HyperlinkedModelSerializer):
    
    

    class Meta:
        model = Caps
        fields =  ('url', 'id','name', 'description', 'price', 'image', 'stock', 'brand')
    def create(self, validated_data):
        cap = Caps.objects.create(**validated_data)
        return cap