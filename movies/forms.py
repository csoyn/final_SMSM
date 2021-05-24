from django import forms
from django.forms import widgets
from .models import Movie, Review, Comment

class ReviewForm(forms.ModelForm):
    CHOICES= [
        (1, '★☆☆☆☆'),
        (2, '★★☆☆☆'),
        (3, '★★★☆☆'),
        (4, '★★★★☆'),
        (5, '★★★★★')
    ]
    rank = forms.IntegerField(
        label='별점',
        widget=forms.Select(
            choices = CHOICES,
            attrs={
                'style': 'width: 10rem;'
            }
        )
    )
    title = forms.CharField(
        label='글 제목',
        widget=forms.TextInput(
            attrs={'style': 'height: 2rem;' , 'class': 'form-control'}
        )
    )
    content = forms.CharField(
        label='글 내용',
        widget=forms.Textarea(
            attrs={'style': 'height: 10rem;', 'class': 'form-control'}
        )
    )
    class Meta:
        model = Review
        fields = ['title', 'rank', 'content',]


class CommentForm(forms.ModelForm):
    content = forms.CharField(
        widget=forms.Textarea(
            attrs={'style': 'height: 2rem;', 'class': 'form-control'}
        )
    )
    class Meta:
        model = Comment
        fields = ('content', )
    
