from django.urls import path, re_path
from users import views  # Asegúrate de importar tus vistas

urlpatterns = [
    path('users/', views.UserList.as_view(), name='user-list'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('users/create/', views.UserCreate.as_view(), name='customuser-create'),

    path('users/<int:pk>/', views.UserDetail.as_view(), name='customuser-detail'),
]