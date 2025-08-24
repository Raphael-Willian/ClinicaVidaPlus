from django.contrib.auth.backends import ModelBackend
from profissionais.models import Profissional

class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        email = kwargs.get("email") or username
        try:
            user = Profissional.objects.get(email=email)
        except Profissional.DoesNotExist:
            return None
        if user.check_password(password) and user.is_active:
            return user
        return None
