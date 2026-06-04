from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import AccessToken

class AuthService:
    @staticmethod
    def validate_jwt(token):
        try:
            token = AccessToken(token)
            user_id = token['user_id']
            user = User.objects.get(id=user_id)
            return {
                "is_valid": True,
                "id": user.id,
                "username": user.username,
                "email": user.email,
            }
        except Exception as e:
            print(f"Token validation error: {e}")
            return {"is_valid": False}