from django.db import models
from django.utils import timezone

class TLE(models.Model):
    title = models.CharField(max_length=255)
    importance = models.IntegerField(default=1)
    start_at = models.DateTimeField(
        verbose_name='',
        editable = True,
        blank=True,
        null=True,
        default = timezone.now
    )
    end_at = models.DateTimeField(
        verbose_name='',
        editable = True,
        blank=True,
        null=True,
        default = timezone.now
        )

    def __str__(self):
        return self.title
