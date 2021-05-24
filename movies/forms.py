from django import forms
from django.forms import widgets
from .models import Movie, Review, Comment

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('title', 'rank', 'content',)
        widgets = {
            'title': forms.TextInput(attrs= {'class': 'form-control'}),
            'rank': forms.Select(attrs= {'class': 'form-control'}),
            'content': forms.Textarea(attrs= {'class': 'form-control'}),
        }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content', )
        widgets = {
            'content': forms.Textarea(attrs= {'class': 'form-control'}),
        }
