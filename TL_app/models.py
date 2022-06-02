from pyexpat import model
from turtle import title
from django.db import models
from django.utils import timezone

GENRE_CHOICES = (
    ('people', '人物'),
    ('Corporate', '企業'),
    ('school', '学校'),
    ('sport', 'スポーツ'),
    ('science', '科学'),
    ('culture', '文化'),
    ('nature', '自然'),
    ('politics・economy', '政治・経済'),
    ('nation・city', '国家・都市'),
    ('region', '地域'),
    ('religion', '宗教'),
    ('organization', '団体'),
    ('space', '宇宙'),
    ('other', 'その他'),
)

class TL(models.Model):
    title = models.CharField(max_length=255)
    english = models.CharField(max_length=255)
    genre = models.CharField(max_length=255, choices=GENRE_CHOICES, default ='')
    date = models.DateTimeField(
        verbose_name='',
        editable = True,
        blank=True,
        null=True,
        default = timezone.now
    )
    abstract = models.TextField(default ='')
    #img
    body = models.TextField(default ='')
    #inline = models.ManyToManyField
    #outline = models.ManyToManyField


    def __str__(self):
        return self.title

class Year(models.Model):
    title = models.CharField(max_length=255)
    year = models.IntegerField()
    TL = models.ManyToManyField(TL, blank=True)

    class Meta:
        ordering = ['year']

    def __str__(self):
        return self.title


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
    parent = models.ForeignKey(
        TL,
        on_delete=models.CASCADE,
        editable = True,
        default=1
    )
    year = models.ForeignKey(
        Year, on_delete=models.CASCADE, editable = True, blank=True
    )

    def __str__(self):
        return self.title

