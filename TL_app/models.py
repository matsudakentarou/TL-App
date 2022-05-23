from django.db import models

class TLE(models.Model):
    title = models.CharField('タイトル', max_length=255)
    

    def __str__(self):
        return self.title