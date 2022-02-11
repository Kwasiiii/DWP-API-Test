from django.urls import path
from .views import UserListView, UsersNearLondon

urlpatterns = [
    path('users/', UserListView.as_view()),
    path('nearlondon/', UsersNearLondon.as_view())
]