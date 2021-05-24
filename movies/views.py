from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_safe, require_http_methods, require_GET, require_POST
from .models import Movie, Review
from .forms import ReviewForm, CommentForm

def movie_index(request):
    movies = Movie.objects.all()
    popular_movies = Movie.objects.all().order_by('vote_average')
    context = {
            'movies': movies,
            'popular_movies' : popular_movies,
        }
    return render(request, 'movies/movie_index.html', context)

# 영화 상세 페이지
# @require_GET
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review_form = ReviewForm()
    reviews = movie.review_set.all()
    context = {
        'movie': movie,
        'review_form' : review_form,
        'reviews' : reviews
    }
    return render(request, 'movies/movie_detail.html', context)

# Review create

@require_POST
def create(request, movie_pk):
    form = ReviewForm(request.POST)
    movie = get_object_or_404(Movie, pk = movie_pk)
    if form.is_valid():
        review = form.save(commit=False)
        review.movie_title = movie
        review.user = request.user
        review.rank = 1
        review.save()
        return redirect('movies:movie_detail', movie.pk)


def detail(request, movie_pk, review_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)
    comments = review.comment_set.order_by('-pk')
    comment_form = CommentForm()
    context = {
        'movie' : movie,
        'review': review,
        'comment_form': comment_form,
        'comments': comments
    }
    return render(request, 'movies/review_detail.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, movie_pk, review_pk ):
    movie = get_object_or_404(Movie, pk=movie_pk)
    review = get_object_or_404(Review, pk=review_pk)

    if request.user == review.user:
        if request.method =="POST":
            form = ReviewForm(request.POST, instance=review)
            if form.is_valid():
                form.save(commit=False)
                review.rank = 1
                form.save()
                return redirect('movies:movie_detail', movie.pk )
        else:
            form = ReviewForm(instance=review)
    # else:
    #     return redirect('movies:movie_index')
    context = {
        'form': form,
        'review' : review,   
    }
    return render(request, 'movies/update.html', context)

@require_POST
def delete(request, movie_pk ,review_pk):
    review = get_object_or_404(Review, pk = review_pk)
    if request.user.is_authenticated:
        if request.user == review.user:
            review.delete()
            return redirect('movies:movie_detail', movie_pk)
        return redirect('movies:movie_detail', movie_pk)

@require_POST
def comments_create(request, movie_pk ,review_pk ):
    if request.user.is_authenticated:
        movie = get_object_or_404(Movie, pk=movie_pk)
        review = get_object_or_404(Review, pk=review_pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.review = review
            comment.user = request.user
            comment.save()
        return redirect('movies:detail', movie.pk, review.pk)
    return redirect('accounts:login')
# movies/views.py 아랫부분에 추가 (미완성)

# @login_required
# def recommend(request):
#     recommended_movies = Movie.objects.filter(genre_id=)[0:2]
#     context = {
#         'recommended_movies' : recommended_movies
#     }
#     return render(request, 'movies/recommend.html', context)

