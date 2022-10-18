from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

# Create your models here.



class User(AbstractUser):
    is_online=models.BooleanField(default=False)
    
    
class Message(models.Model):
    message = models.CharField(max_length=500)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)
