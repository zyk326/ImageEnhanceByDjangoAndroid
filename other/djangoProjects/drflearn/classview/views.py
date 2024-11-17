from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import MerchantSerializer
from meituan.models import Merchant
from rest_framework import status

##########APIView's code####################
# class MerchantView(APIView):
#     def get_object(self, pk):
#         try:
#             return Merchant.objects.get(pk=pk)
#         except Merchant.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk=None):
#         if pk:
#             merchant = self.get_object(pk)
#             serializer = MerchantSerializer(merchant)
#             return Response(serializer.data)
#         else:
#             queryset = Merchant.objects.all()
#             serializer = MerchantSerializer(instance=queryset, many=True)
#             return Response(serializer.data)
#
#     def put(self, request, pk):
#         merchant = self.get_object(pk)
#         serializer = MerchantSerializer(merchant, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk):
#         merchant = self.get_object(pk)
#         merchant.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

##########Mixin's code####################
# from rest_framework import generics
# from rest_framework import mixins
# class MerchantView(
#     generics.GenericAPIView, #basic
#     mixins.ListModelMixin,  #全部查询
#     mixins.RetrieveModelMixin, #pk查询
#     mixins.CreateModelMixin,    #新增
#     mixins.UpdateModelMixin,    #更新
#     mixins.DestroyModelMixin
# ):
#     queryset = Merchant.objects.all()
#     serializer_class = MerchantSerializer
#
#     def get(self, request, pk=None):
#         if pk:
#             return self.retrieve(request)
#         else:
#             return self.list(request)
#
#     # 重写的保存逻辑在这里
#     # def perform_create(self, serializer):
#     #     serializer.save(created=self.request.user)
#
#     def post(self, request):
#         return self.create(request)
#
#     def put(self, request, pk):
#         return self.update(request, pk)
#
#     def delete(self, request, pk):
#         return self.destroy(request, pk)

#########Generic's code####################
from rest_framework import generics
class MerchantView(
    generics.ListAPIView,
    generics.CreateAPIView,
    generics.UpdateAPIView,
    generics.DestroyAPIView,
):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

##########View's code####################
from rest_framework import viewsets
from rest_framework.decorators import action
class MerchantViewSet(viewsets.ModelViewSet):
    queryset = Merchant.objects.all()
    serializer_class = MerchantSerializer

    @action(['GET'], detail=False,url_path='cs')
    def changeshang(self, request):
        queryset = self.get_queryset()
        serializer_class = self.get_serializer_class()
        result = queryset.filter(name__contains='长沙')
        serializer = serializer_class(result, many=True)
        return Response(serializer.data)