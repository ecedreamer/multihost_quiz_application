from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import *
from .utils import *


# authentication apis: register, login, profile

class UserLoginAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        response = {
            "success": False,
            "msg": "Invalid user credentials"
        }
        if serializer.is_valid():
            user = authenticate(**serializer.data)
            if user is not None:
                response = get_tokens_for_user(user)
                return Response(response, status=status.HTTP_200_OK)
        else:
            response = serializer.errors
        return Response(response, status=status.HTTP_401_UNAUTHORIZED)


class UserProfileAPIView(APIView):
    permission_classes = [UserOnlyPermission, ]

    def get(self, request, *args, **kwargs):
        serializer = UserProfileSerializer(request.user)
        response = serializer.data
        return Response(response, status=status.HTTP_200_OK)

# quiz session apis : list, detail, create, update, delete





# question apis: create, update and delete


# quiz play api and submit api
class QuizSessionPlayAPIView(APIView):
    permission_classes = [UserOnlyPermission, ]

    def get(self, request, unique_code, *args, **kwargs):
        quiz_session = QuizSession.objects.get(unique_code=unique_code)
        serializer = QuizSessionPlaySerializer(quiz_session)
        return Response(serializer.data, status=status.HTTP_200_OK)