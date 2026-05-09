from django.db.models import Model
from rest_framework import mixins, viewsets, generics
from django.http import JsonResponse

from cart.models import CartSession, CartItem
from cart.serializers import CartSessionSerializer, CartItemSerializer


# Create your views here.

class CartSessionView(mixins.ListModelMixin, mixins.RetrieveModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = CartSession.objects.all()
    serializer_class = CartSessionSerializer

class CartItemViewList(generics.ListCreateAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
class CartItemViewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
