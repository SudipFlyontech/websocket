from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, BaseUserManager

# Create your models here.


# User = get_user_model()

class UserManager(BaseUserManager):

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_staff = True
        user.is_superuser = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=250)
    password2 = models.CharField(max_length=250)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [] 
    objects = UserManager()


class Message(models.Model):
    message = models.JSONField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, null=True, blank=True)

