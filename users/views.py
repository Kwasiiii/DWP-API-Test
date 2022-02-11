from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from .serializers.common import UserSerializer
# Create your views here.

class UserListView(APIView):

    def get(self, _request):
        users = requests.get('https://bpdts-test-app.herokuapp.com/users').json()
        print(users)
        serialized_users = UserSerializer(users, many = True)
        print(serialized_users.data)
        return Response(serialized_users.data, status=status.HTTP_200_OK)
