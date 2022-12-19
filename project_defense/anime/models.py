from django.core.validators import MinLengthValidator
from django.db import models
from django.utils import timezone

from project_defense.profileapp.models import AppUser


class AnimeTorrent(models.Model):
    ANIME_MAX_CHARS = 40
    ANIME_MIN_CHARS = 2

    HORROR = 'Horror'
    FANTASY = 'Fantasy'
    ACTION = 'Action'
    SCI_FI = 'Sci-fi'
    WHOLESOME = 'Wholesome'
    COMEDY = 'Comedy'
    GENRE = [(x, x) for x in (HORROR, FANTASY, ACTION, SCI_FI, WHOLESOME, COMEDY)]
    GENRE_MAX_CHARS = max(len(x) for _, x in GENRE)

    name = models.CharField(
        max_length=ANIME_MAX_CHARS,
        validators=(
            MinLengthValidator(ANIME_MIN_CHARS),
        ),
    )

    genre = models.CharField(
        max_length=GENRE_MAX_CHARS,
        choices=GENRE,
    )

    image_field = models.URLField(
        null=True,
    )

    date_of_upload = models.DateTimeField(
        editable=False,
    )

    date_of_last_download = models.DateTimeField(
        null=True,
        blank=True,
    )

    download_count = models.PositiveIntegerField(
        default=0,
    )

    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    uploader = models.ForeignKey(
        AppUser,
        on_delete=models.CASCADE,
    )

    def save(self, *args, **kwargs):
        # On save, update timestamps and update download count
        if not self.pk:
            self.date_of_upload = timezone.now()
            return super(AnimeTorrent, self).save(*args, **kwargs)
        self.date_of_last_download = timezone.now()
        self.download_count += 1
        return super(AnimeTorrent, self).save(*args, **kwargs)
