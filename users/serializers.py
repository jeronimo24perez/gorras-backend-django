from django.contrib.auth.models import Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token
from users.models import CustomUser


class UserSerializer(serializers.HyperlinkedModelSerializer):
    token = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = CustomUser
        fields = ('url', 'username', 'email', 'password', 'token', 'groups')
        extra_kwargs = {'password': {'write_only': True}}

    def get_token(self, obj):
        token, created = Token.objects.get_or_create(user=obj)
        return token.key

    def create(self, validated_data):
        # Extraemos los grupos si es que vienen en la petición
        groups_data = validated_data.pop('groups', [])

        # Usamos 'create_user' en lugar del create normal.
        # Esta función interna de Django es la que aplica la encriptación automáticamente.
        user = CustomUser.objects.create_user(**validated_data)

        if groups_data:
            user.groups.set(groups_data)

        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')

