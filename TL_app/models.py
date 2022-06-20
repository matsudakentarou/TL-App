from distutils.command.upload import upload
from email.policy import default
from pyexpat import model
from turtle import title
from django.db import models
from django.utils import timezone
from django.core.validators import MaxValueValidator, MinValueValidator

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
    start_year = models.IntegerField(default=1800)
    end_year = models.IntegerField(default=1800)
    abstract = models.TextField(default ='')
    tagimage = models.ImageField(upload_to='images', blank=True, null=True)
    mainimage = models.ImageField(upload_to='images', blank=True, null=True)
    body = models.TextField(default ='')
    #inline = models.ManyToManyField
    #outline = models.ManyToManyField


    def __str__(self):
        return self.title


class TLE(models.Model):
    title = models.CharField(max_length=255)
    parent = models.ForeignKey(
        TL,
        on_delete=models.CASCADE,
        editable = True,
        default=1
    )
    year = models.IntegerField(default=1800)
    rank = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(3)], default=1)
    image = models.ImageField(upload_to='images', blank=True, null=True)
    video = models.TextField(default ='', blank=True, null=True)
    map = models.TextField(default ='', blank=True, null=True)
    body = models.TextField(default ='', blank=True, null=True)

    def __str__(self):
        return self.title

