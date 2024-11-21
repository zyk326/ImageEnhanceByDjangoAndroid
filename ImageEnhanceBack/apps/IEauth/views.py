from rest_framework.views import APIView
from .serializers import LoginSerializer, UserSerializer, RegisterSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data.get('user')
            user.save()
            return Response({'user' : UserSerializer(user).data})
        else:
            detail = list(serializer.errors.values())[0][0]
            print(serializer.errors)
            return Response({"detail": detail}, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({'user' : UserSerializer(user).data})
        else:
            detail = list(serializer.errors.values())[0][0]
            print(serializer.errors)
            return Response({"detail": detail}, status=status.HTTP_400_BAD_REQUEST)