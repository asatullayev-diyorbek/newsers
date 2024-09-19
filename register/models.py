from django.db import models
from django.contrib.auth.models import User


class UserConfirmation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    confirmation_code = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Confirmation code for {self.user.username}"

    class Meta:
        verbose_name = "Tasdiqlash kodi"
        verbose_name_plural = "Tasdiqlash kodlari"

    @staticmethod
    def generate_confirmation_code():
        import random
        code = ""
        for _ in range(6):
            code += str(random.randint(0, 9))
        return code