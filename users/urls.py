from django.urls import path
from .views import UserListView, UsersNearLondon

urlpatterns = [
    path('users/', UserListView.as_view()), #path to retrieve all users information
    path('nearlondon/', UsersNearLondon.as_view()) #path to retrieve users within 50 miles from London
]