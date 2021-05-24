from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENRE_CHOICES = (
        ('판타지', '판타지'),
        ('드라마', '드라마'),
        ('공포', '공포'),
        ('액션', '액션'),
        ('코미디', '코미디'),
        ('스릴러', '스릴러'),
        ('범죄', '범죄'),
        ('로맨스', '로맨스'),
        ('SF', 'SF'),
    )
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    gender = models.TextField(choices=[
        ('남', '남'),
        ('여', '여'),
        ('불특정', '불특정'),
    ])
    like_genre = models.TextField(choices = GENRE_CHOICES)
    profile_image = models.ImageField(default='man1.png')

