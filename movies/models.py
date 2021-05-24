from django.db import models
from django.conf import settings

class Genre(models.Model):
    name = models.TextField()
    
class Movie(models.Model):
    title = models.TextField()
    poster_path = models.TextField()
    overview = models.TextField()
    genre_ids = models.ManyToManyField(Genre, related_name='movie_genre')
    popularity = models.FloatField()
    release_date = models.DateField()
    vote_average = models.IntegerField()
    original_title = models.TextField()

class Review(models.Model):
    movie_title = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    rank = models.IntegerField(blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    review = models.ForeignKey(Review, on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
