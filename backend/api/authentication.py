from django.contrib.auth.backends import ModelBackend
from .models import UserData  
from django.contrib.auth.hashers import check_password

class EmailBackend(ModelBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = UserData.objects.get(email=email)
        except UserData.DoesNotExist:
            return None

        if user and check_password(password, user.password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return UserData.objects.get(pk=user_id)
        except UserData.DoesNotExist:
            return None
