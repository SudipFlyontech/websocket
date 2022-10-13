from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models

# Create your models here.
User = get_user_model()

class Message(models.Model):
    message = models.JSONField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)


# class LoggedInUser(models.Model):
#     user = models.OneToOneField(
#         settings.AUTH_USER_MODEL, related_name='logged_in_user')