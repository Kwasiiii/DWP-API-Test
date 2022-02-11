from math import sqrt
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

class UsersNearLondon(APIView):

    
    def get(self, _request):
        london_lat = 51.507
        london_long = -0.128

        lat_miles = 69.2
        long_miles = 43.00
        users = requests.get('https://bpdts-test-app.herokuapp.com/users').json()
        print(len(users))
        in_or_not = [user for user in users if abs(float(user['latitude']) - london_lat  * lat_miles) <= 50 or abs(float(user['longitude']) - london_long * long_miles) <= 50]
        print(len(in_or_not))
        in_or_within = [user for user in in_or_not if sqrt((float(user['latitude']) - london_lat  * lat_miles) * (float(user['latitude']) - london_lat  * lat_miles)) + ((float(user['longitude']) - london_long * long_miles) * (float(user['longitude']) - london_long * long_miles))]
        print(len(in_or_within))
        serialized_users = UserSerializer(in_or_within, many = True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)
