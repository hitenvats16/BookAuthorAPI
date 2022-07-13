# URL Mappings for the author api

from django.urls import path

from . import views

from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # for getting authentication token
    path('token/', obtain_auth_token, name='token'),
    # for getting current users info
    path('me/', views.ManageUserView.as_view(), name='me'),
    # for getting list of all users(authors)
    path('', views.AuthorList, name='Authors'),
]
