from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager
from django.db import models


class  UserManager(BaseUserManager):
     def create_user(self,email,password,**extra_fields):
          if not email:
               raise ValueError("You must provide email address")
          if not password:
               raise ValueError("you must provide passsword ")
          if not extra_fields.get("username"):
               raise ValueError("username must be provided")
          
          email = self.normalize_email(email)
          user = self.model(email=email,**extra_fields)
          user.set_password(password)
          user.save()
          return user
     def create_superuser(self,email,password,username=None,**extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        if extra_fields.get("is_staff") is not True:
             raise ValueError("Staff permission must be True")
        if extra_fields.get("is_superuser") is not True:
             raise ValueError("Super permission must be True")

        return self.create_user(email,password,username=username,**extra_fields)


class RifUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=150,unique=True,null=False,blank=False,default=None)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']  # nothing extra required on createsuperuser

    def __str__(self):
        return self.username