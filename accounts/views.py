from rest_framework import generics, permissions
from django.contrib.auth import get_user_model
from .serializers import UserCreateSerializer, UserLoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import views
from django.contrib.auth import authenticate, logout, login


User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    serializer_class = UserCreateSerializer
    queryset = User.objects.all()

    permission_classes = [permissions.AllowAny]


class LoginView(views.APIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = UserLoginSerializer

    def post(self, request):
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

    def get(self, request):
        logout(request)
        return Response({}, status=status.HTTP_204_NO_CONTENT)

