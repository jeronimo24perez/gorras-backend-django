from django.contrib import admin

from cart.models import CartSession, CartItem

# Register your models here.
admin.site.register(CartSession)
admin.site.register(CartItem)