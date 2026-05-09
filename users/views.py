from django.http import JsonResponse
from rest_framework import  generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from users.models import CustomUser
from users.serializers import UserSerializer
from users.services import auth_user_service
# Create your views here.


@api_view(['POST'])
def login(request):
    email = request.data.get('email')
    password = request.data.get('password')

    try:
        token = auth_user_service(email, password)
        return JsonResponse({"token": token}, status=status.HTTP_200_OK)
    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request):
    user = get_object_or_404(CustomUser, email=request.data['email'])
    serializer = UserSerializer(instance=user, context={'request': request})

    return JsonResponse({"message": serializer.data}, status=200)


class UserList(generics.ListCreateAPIView):
   queryset = CustomUser.objects.all()
   serializer_class = UserSerializer


class UserDetail(
  generics.RetrieveUpdateDestroyAPIView
):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticatedOrReadOnly]