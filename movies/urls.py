from django.urls import path
from . import views

app_name="movies"
urlpatterns = [
    # 전체 영화 목록
    path('', views.movie_index, name='movie_index'),
    # 영화 상세 페이지
    path('<int:movie_pk>/', views.movie_detail, name='movie_detail'),

    # Review create
    path('<int:movie_pk>/create/', views.create, name='create'),
    # Review detail
    path('<int:movie_pk>/detail/<int:review_pk>', views.detail, name='detail'),
    # Review delete
    path('<int:movie_pk>/delete/<int:review_pk>', views.delete, name='delete'),
    # Review update
    path('<int:movie_pk>/update/<int:review_pk>', views.update, name='update'),
   
    # Comment create
    path('<int:movie_pk>/<int:review_pk>/comments/create', views.comments_create, name='comments_create'),
    # # Comment delete
    # path('<int:movie_pk>/<int:review_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name='comments_delete'),
    # # Review likes
    # path('<int:review_pk>/likes/', views.likes, name='likes'),
    # path('recommend/', views.recommend, name='recommend'),

]
