from rest_framework import permissions, views, status
from rest_framework.response import Response
from django.contrib.auth import authenticate, logout, login

from .serializers import UserCreateSerializer, UserLoginSerializer


class UserCreateView(views.APIView):
    permission_classes = [permissions.AllowAny]

    @staticmethod
    def post(request):
        serializer = UserCreateSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            if user:
                return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    @staticmethod
    def post(request):
        user = authenticate(
            username=request.data.get("username"),
            password=request.data.get("password"),
        )
        if user is None or not user.is_active:
            return Response({
                'message': 'Username or password incorrect'
            }, status=status.HTTP_401_UNAUTHORIZED)
        login(request, user)
        return Response(UserLoginSerializer(user).data)


class LogoutView(views.APIView):

    @staticmethod
    def get(request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

