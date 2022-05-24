from django.db import models
from pytz import timezone

class TLE(models.Model):
    title = models.CharField('タイトル', max_length=255)
    importance = models.IntegerField(default=1)
    updated_at = models.DateTimeField('更新日時', auto_now=True)

    def __str__(self):
        return self.title
