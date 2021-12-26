from django.urls import path
from . import views

app_name="reviews"

urlpatterns = [
  path("<int:pk>/movie/", views.ReviewView.as_view(), name="review_input"),
  path("<int:pk>/book/", views.ReviewBookView.as_view(), name="review_bookinput"),
  
  path("<int:pk>/<int:movie_pk>/moviedelete", views.delreview, name="delete"),
  path("<int:pk>/<int:book_pk>/bookdelete", views.delbookreview, name="delete_book"),
  
  
]
