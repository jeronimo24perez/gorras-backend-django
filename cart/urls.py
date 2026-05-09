from django.urls import path

from cart.views import CartSessionView, CartItemViewList, CartItemViewDetail

urlpatterns = [
    path('cart_session/', CartSessionView.as_view({'get':'list',  'post': 'create' }), name='cart_session'),
    path('cart_session/<int:pk>/', CartSessionView.as_view({'get':'retrieve'}), name='cart_session_detail'),
    path('cart_item/', CartItemViewList.as_view(), name='cart_item_list'),
    path('cart_item/<int:pk>/', CartItemViewDetail.as_view(), name='cart_item_detail'),
]