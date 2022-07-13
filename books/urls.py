# URL Mappings for the book

from django.urls import path

from . import views

urlpatterns = [
    # List all books
    path('', views.ListBooks.as_view(), name='ListBooks'),  
    # Details of given book with id
    path('<int:id>/', views.GetDetails, name='Details'),
    # Like book with given id
    path('like/<int:id>', views.LikeABook, name='Like'),
    # Unlike book with given id
    path('unlike/<int:id>', views.UnlikeABook,name='Unlike'),  
]
