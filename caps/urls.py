from django.urls import path


from caps.views import Caps_detail, Caps_list, Caps_create

urlpatterns = [
    path('caps/', Caps_list.as_view(), name='caps-list'),
    path('caps/create/', Caps_create.as_view(), name='caps-create'),
    path('caps/<int:pk>/', Caps_detail.as_view(), name='caps-detail'),
]
