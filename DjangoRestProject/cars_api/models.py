from django.contrib.auth.hashers import make_password
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.utils import timezone


class MyUserManager(UserManager):
    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError("The given username must be set")

        user = self.model(username=username, **extra_fields)
        user.password = make_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(username, password, **extra_fields)

    def create_superuser(self, username, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(

        max_length=150,
        unique=True,
        help_text=(
            "Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."
        ),
        validators=[username_validator],
        error_messages={
            "unique": ("A user with that username already exists."),
        },
    )

    email = models.EmailField(
        blank=True
    )
    is_staff = models.BooleanField(

        default=True,
        help_text=("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(

        default=True,

    )
    description = models.TextField(
        null=True,
        blank=True,
    )
    nationality = models.CharField(
        max_length=100,
        null=True,
        blank=True,
    )
    date_joined = models.DateTimeField(default=timezone.now)

    objects = MyUserManager()
    USERNAME_FIELD = "username"


class CarBrand(models.Model):
    name = models.CharField(
        max_length=50,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    deleted_at = models.DateTimeField(
        auto_now=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'{self.name}'


class CarModel(models.Model):
    car_brand = models.ForeignKey(
        CarBrand, on_delete=models.CASCADE
    )
    name = models.CharField(
        max_length=100,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        auto_now=True,
    )
    description = models.TextField(
        null=True,
        blank=True,
    )

    def __str__(self):
        return f"{self.name}"


class UserCar(models.Model):
    user_key = models.ForeignKey(
        User, on_delete=models.CASCADE
    )
    car_brand = models.ForeignKey(
        CarBrand, on_delete=models.CASCADE
    )
    car_model = models.ForeignKey(
        CarModel, on_delete=models.CASCADE
    )
    odometer = models.IntegerField(
        validators=(
            MaxValueValidator(400),
            MinValueValidator(0),
        )
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
    )
    deleted_at = models.DateTimeField(
        auto_now=True,
    )
    horse_power = models.IntegerField(
        validators=(
            MaxValueValidator(300),
            MinValueValidator(0),
        )
    )
    color = models.CharField(
        max_length=50,
    )
    price = models.FloatField(
        validators=(
            MinValueValidator(0.0),
        )
    )

    def __str__(self):
        return f'{self.car_brand} {self.car_model}'
