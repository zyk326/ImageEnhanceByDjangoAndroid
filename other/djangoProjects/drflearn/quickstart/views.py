from rest_framework import viewsets

from meituan.models import Merchant

from .serializers import MerchantSerializer

# 增删改检索都做了
class MerchantViewset(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer