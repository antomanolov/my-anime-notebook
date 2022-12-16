from django.contrib.auth.models import AbstractUser
from django.core.validators import MinLengthValidator
from django.db import models


class AppUser(AbstractUser):
    MAX_CHARS_FIRST_NAME = 30
    MIN_CHARS_FIRST_NAME = 2
    MAX_CHARS_LAST_NAME = 30
    MIN_CHARS_LAST_NAME = 2
    DEFAULT_ZERO_VALUE = 0

    profile_picture = models.URLField()

    email = models.EmailField(
        unique=True,
    )

    first_name = models.CharField(
        max_length=MAX_CHARS_FIRST_NAME,
        validators=(
            MinLengthValidator(MIN_CHARS_FIRST_NAME),
        )
    )

    last_name = models.CharField(
        max_length=MAX_CHARS_LAST_NAME,
        validators=(
            MinLengthValidator(MIN_CHARS_LAST_NAME),
        )
    )

    uploaded_count = models.PositiveIntegerField(
        default=DEFAULT_ZERO_VALUE,
    )

    downloaded_count = models.PositiveIntegerField(
        default=DEFAULT_ZERO_VALUE,
    )

    total_screenshots = models.PositiveIntegerField(
        default=DEFAULT_ZERO_VALUE,
    )
