from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from meituan.models import Merchant
from .authentications import generate_jwt
from .serializers import MerchantSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import get_user_model

User = get_user_model()

class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

@api_view(['GET'])
def token_view(request):
    token = generate_jwt(User.objects.first())
    return Response({'token': token})