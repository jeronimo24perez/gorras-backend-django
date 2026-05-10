from django.db.models import Model
from rest_framework import mixins, viewsets, generics
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated

from cart.models import CartSession, CartItem
from cart.serializers import CartSessionSerializer, CartItemSerializer


# Create your views here.

class CartSessionView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CartSession.objects.all()
    serializer_class = CartSessionSerializer

    permission_classes = [IsAuthenticated]

class CartItemViewList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    permission_classes = [IsAuthenticated]
class CartItemViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer

    permission_classes = [IsAuthenticated]
