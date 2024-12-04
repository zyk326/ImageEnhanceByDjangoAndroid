from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UploadImageSerializer
from shortuuid import uuid
import os
from django.conf import settings
from rest_framework.response import Response
from .utils import image_enhance


# Create your views here.
class UploadImage(APIView):
    def post(self, request):
        serializer = UploadImageSerializer(data=request.data)
        if serializer.is_valid():
            file = serializer.validated_data.get('image')
            filename = uuid() + os.path.splitext(file.name)[-1]
            path = settings.MEDIA_ROOT / filename
            try:
                with open(path, 'wb') as fp:
                    for chunk in file.chunks():
                        fp.write(chunk)
            except:
                return Response({
                    "errno" : 1,
                    "message": "图片保存失败!"
                })
            print("beforeEnhance path is:", path)
            after_deal_file_path = image_enhance(path)
            print("afterEnhance path is:", after_deal_file_path)
            return Response({
                "errno": 0,  # 注意：值是数字，不能是字符串
                "data": {
                    "url": after_deal_file_path,  # 图片src ，必须
                    "alt": "",  # 图片描述文字，非必须
                    "href": after_deal_file_path  # 图片的链接，非必须
                }
            })
        else:
            print(serializer.errors)
            return Response({
                "errno": 1,
                "message": list(serializer.errors.values())[0][0]
            })