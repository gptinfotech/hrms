from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import serializers
from .models import Users
from django.shortcuts import get_object_or_404
from django.db import IntegrityError
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AllUsersView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # Fetch all users
        users = Users.objects.all()
        serializer = UserRegistrationSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = Users.objects.get(email=serializer.validated_data['email'])
            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": {
                    "user_id": user.user_id,  #
                    "email": user.email,
                    "username": user.username,
                    "user_type": user.user_type,
                },
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from django.http import JsonResponse
from django.core.serializers import serialize
from .models import Users

def view_all_users(request):
    if request.method == "GET":
        # Fetch all user records
        users = Users.objects.all()
        # Serialize user data into a JSON-compatible format
        user_data = [
            {
                "user_id": user.user_id,
                "email": user.email,
                "username": user.username,
                "fullname": user.fullname,
                "user_type": user.user_type,
                "qualification": user.qualification,
                "passing_year": user.passing_year,
                "address": user.address,
                "is_active": user.is_active,
                "created_at": user.created_at,
                "updated_at": user.updated_at,
                "password" : user.password,
            }
            for user in users
        ]
        return JsonResponse({"users": user_data}, safe=False)
    return JsonResponse({"error": "Invalid request method"}, status=400)
