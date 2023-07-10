from django.urls import path
from rental_service import views

urlpatterns=[
    path('',views.MovieList.as_view(),name="movie-list"),
    path('<int:pk>',views.MovieDetail.as_view(),name="movie-detail"),
]