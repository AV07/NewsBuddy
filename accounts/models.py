from django.db import models
from django.contrib.auth.models import AbstractBaseUser,PermissionsMixin,BaseUserManager
# Create your models here.

class UserAccountManager(BaseUserManager):
    def create_user(self,email,password,name):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            password=password,
            name = name,
            )
        user.set_password(password)
        user.save()

        return user
    
    def create_superuser(self,email,password,**other_fields):
        user = self.create_user(email,password,**other_fields)

        user.is_staff = True
        user.is_superuser = True
        user.access = 0
        user.save()

        return user


class UserAccount(AbstractBaseUser,PermissionsMixin):
    id = models.AutoField(primary_key=True)
    email = models.EmailField(max_length=50, unique=True)
    name = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name", ]

    def get_full_name(self):
        return self.name 

    def get_short_name(self):
        return self.name 

    def __str__(self):
        return self.email
