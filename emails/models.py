
from django.db import models
import uuid
from config import settings
# Create your models here.

class Email(models.Model):
    email = models.EmailField(unique=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)


class EmailVerificationEvent(models.Model):
    parent = models.ForeignKey(Email,on_delete=models.SET_NULL,null=True)
    email = models.EmailField()
    token = models.UUIDField(default=uuid.uuid1)
    attempts = models.IntegerField(default=0)
    last_attempt_at = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    expired = models.BooleanField(default=False)
    expired_at = models.DateTimeField(auto_now_add=False,auto_now=False,blank=True,null=True)
    datetime_created = models.DateTimeField(auto_now_add=True)
    @property
    def verifey_link(self):
        return f'{settings.BASE_DOMAIN}/verifey/{self.token}'