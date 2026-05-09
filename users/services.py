
from django.forms import ValidationError
from rest_framework.authtoken.models import Token
from users.models import CustomUser


def auth_user_service(email, password):
    try:
        user = CustomUser.objects.get(email=email)
    except CustomUser.DoesNotExist:
        raise ValidationError("Invalid email or password")
    if not user.check_password(password):
        raise ValidationError("Invalid email or password")
    token, created = Token.objects.get_or_create(user=user)
    return token.key