from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from django.forms import fields, widgets
from django import forms
from .models import User

user = get_user_model()

class CustomUserChangeForm(UserChangeForm):
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
    like_genre = forms.Select(attrs={'class': 'form-control'}, choices=GENRE_CHOICES)
    class Meta:
        model = user
        fields = ('username', 'profile_image',)
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
        }

class CustomUserCreationForm(UserCreationForm):
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
    GENDER_CHOICES = (
        ('남', '남'),
        ('여', '여'),
        ('불특정', '불특정'),
    )
    like_genre = forms.Select(attrs={'class': 'form-control'}, choices=GENRE_CHOICES)
    gender = forms.Select(attrs={'class': 'form-control'}, choices=GENDER_CHOICES)
    class Meta:
        model = user
        fields = ('username', 'like_genre', 'gender',)
        widgets = {'username' : forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : '아이디를 입력하세요'}),
                'like_genre': forms.Select(attrs={'class':'form-control'}),
                'gender': forms.Select(attrs={'class' : 'form-control', 'placeholder' : '성별을 선택하세요'})}