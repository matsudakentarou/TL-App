from django.db import models
from pytz import timezone

class TLE(models.Model):
    title = models.CharField('タイトル', max_length=255)
    importance = models.IntegerField(default=1)
    start_at = models.DateTimeField('開始日時', auto_now=True)
    end_at = models.DateTimeField('終了日時', auto_now=True)

    def __str__(self):
        return self.title
