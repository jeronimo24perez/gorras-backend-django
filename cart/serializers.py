from rest_framework import serializers

from cart.models import CartSession, CartItem


class CartSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartSession
        fields = (
            'id',
            'user',
            'createdAt',
            'status'
        )
        many = True

class CartItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartItem
        fields = (
            'id',
            'cart',
            'product',
            'quantity'
        )
        many = True
