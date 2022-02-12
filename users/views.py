from math import radians, cos, sin, asin, sqrt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import requests

from .serializers.common import UserSerializer

class UserListView(APIView):

    # Retrive all users information from external API. 
    def get(self, _request):
        users = requests.get('https://bpdts-test-app.herokuapp.com/users').json()
        print(users)
        serialized_users = UserSerializer(users, many = True)
        print(serialized_users.data)
        return Response(serialized_users.data, status=status.HTTP_200_OK)

class UsersNearLondon(APIView):

    # This returns the distance between two bearings(GPS points) 
    def haversine(self, lat1, lon1, lat2, lon2):

        R = 3959.87433 # this is in miles.

        dLat = radians(lat2 - lat1)
        dLon = radians(lon2 - lon1)
        lat1 = radians(lat1)
        lat2 = radians(lat2)

        a = sin(dLat/2)**2 + cos(lat1)*cos(lat2)*sin(dLon/2)**2
        c = 2*asin(sqrt(a))
        
        result = R * c
        return result
    
    def get(self, _request):
        # Latitude and Longitude of London
        london_lat = 51.507
        london_long = -0.128
        
        # Maximum distance in miles from london
        max_distance = 50

        # HTTP request to retrieve all user information from external API.
        users = requests.get('https://bpdts-test-app.herokuapp.com/users').json()
        print(users) 

        # Filter data retrieved from data the HTTP request with condition if the distance between london and user location is less than or equal to 50
        users_within_fifty_miles = [user for user in users if self.haversine(london_lat, london_long, float(user['latitude']), float(user['longitude'])) <= max_distance]
        print(users_within_fifty_miles)

        # Passing results(users within fifty miles) through as serializer to be displayed
        serialized_users = UserSerializer(users_within_fifty_miles, many = True)
        return Response(serialized_users.data, status=status.HTTP_200_OK)
