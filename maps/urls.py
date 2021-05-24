from django.urls import path
from . import views


app_name = 'maps'
urlpatterns = [
    path('search/', views.search, name='search'),
]