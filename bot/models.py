from django.db import models
from django.db.models import BigIntegerField, CharField, OneToOneField
from django.utils.crypto import get_random_string
from core.models import User


class TgUser(models.Model):
    tg_chat_id: BigIntegerField = models.BigIntegerField(primary_key=True, editable=False, unique=True)
    username: CharField = models.CharField(max_length=255, null=True, blank=True)
    user: OneToOneField = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    verification_code: CharField | None = models.CharField(max_length=20, unique=True, null=True, blank=True)

    @property
    def is_verified(self) -> bool:
        return bool(self.user)

    @staticmethod
    def _generate_verification_code() -> str:
        return get_random_string(20)

    def update_verification_code(self) -> None:
        self.verification_code: CharField = self._generate_verification_code()
        self.save(update_fields=["verification_code"])

    def __str__(self):
        return f'{self.__class__.__name__}({self.tg_chat_id})'

    class Meta:
        verbose_name = "Телеграм пользователь"
        verbose_name_plural = "Телеграм пользователи"
