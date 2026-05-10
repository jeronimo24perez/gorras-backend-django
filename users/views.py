from django.http import JsonResponse
from rest_framework import  generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from users.models import CustomUser
from users.serializers import UserSerializer
from users.services import auth_user_service, get_profile_by_token
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
    auth_header = request.META.get('HTTP_AUTHORIZATION')
    try:
        user =  get_profile_by_token(request, auth_header)
        return JsonResponse({"message": user}, status=status.HTTP_200_OK)

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)



class UserList(generics.ListAPIView):
   queryset = CustomUser.objects.all()
   serializer_class = UserSerializer

   permission_classes=  [IsAdminUser]

class UserCreate(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(
  generics.RetrieveUpdateDestroyAPIView
):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

    permission_classes = [IsAuthenticated]