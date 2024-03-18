from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.contrib.auth.hashers import make_password
from django.apps import apps

NULLABLE = {'blank': True, 'null': True}


class UserManager(BaseUserManager):
    pass
    # use_in_migrations = True
    #
    # def _create_user(self, email, password, **extra_fields):
    #     if not email:
    #         raise ValueError("The given username must be set")
    #     email = self.normalize_email(email)
    #     GlobalUserModel = apps.get_model(
    #         self.model._meta.app_label, self.model._meta.object_name
    #     )
    #     email = GlobalUserModel.normalize_username(email)
    #     user = self.model(email=email, **extra_fields)
    #     user.password = make_password(password)
    #     user.save(using=self._db)
    #     return user
    #
    # def create_user(self, email, password=None, **extra_fields):
    #     extra_fields.setdefault("is_staff", False)
    #     extra_fields.setdefault("is_superuser", False)
    #     return self._create_user(email, password, **extra_fields)
    #
    # def create_superuser(self, email, password=None, **extra_fields):
    #     extra_fields.setdefault("is_staff", True)
    #     extra_fields.setdefault("is_superuser", True)
    #
    #     if extra_fields.get("is_staff") is not True:
    #         raise ValueError("Superuser must have is_staff=True.")
    #     if extra_fields.get("is_superuser") is not True:
    #         raise ValueError("Superuser must have is_superuser=True.")
    #
    #     return self._create_user(email, password, **extra_fields)


class UserRole(models.TextChoices):
    MODERATOR = 'moderator'
    MEMBER = 'member'


class User(AbstractUser):
    role = models.CharField(max_length=250, choices=UserRole.choices, default=UserRole.MEMBER)
    username = None
    email = models.EmailField(unique=True, verbose_name='email')
    phone_num = models.CharField(max_length=35, verbose_name='номер телефона', **NULLABLE)
    country = models.CharField(max_length=150, verbose_name='страна', **NULLABLE)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()
