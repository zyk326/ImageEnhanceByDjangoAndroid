# 1.用来序列化
# 2.用来验证表单数据
# 3.可以创建数据,修改数据

# form -> serializer
from rest_framework import serializers

from meituan.models import Merchant, GoodsCategory


# Serializer的:
# instance:用来把[ORM] -> JSON
# data:用来验证数据是否符合要求
# many:如果instance是一个很多的对象,那么many==true

# class MerchantSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(max_length=200, required=True, error_messages={"required":"name必须要传"})
#     address = serializers.CharField(max_length=200, required=True)
#     logo = serializers.CharField(max_length=200, required=True)
#     notice = serializers.CharField(max_length=200, required=False)
#     up_send = serializers.DecimalField(max_digits=6, decimal_places=2, required=False)
#     lon = serializers.FloatField(required=True)
#     lat = serializers.FloatField(required=True)
#
#     # 把instance更新
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.address = validated_data.get('address', instance.address)
#         instance.notice = validated_data.get('notice', instance.notice)
#         instance.logo = validated_data.get('logo', instance.logo)
#         instance.up_send = validated_data.get('up_send', instance.up_send)
#         instance.lon = validated_data.get('lon', instance.lon)
#         instance.lat = validated_data.get('lat', instance.lat)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         return Merchant.objects.create(**validated_data)  # 字典变成关键字参数，用**： {} -》 name='zyk'

class MerchantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merchant
        fields = '__all__'
        # exclude = ["name"] #排除name

class GoodsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = '__all__'

class GoodsCategorySerializer(serializers.ModelSerializer):
    merchant = MerchantSerializer(read_only=True) # 查外键的时候需要用到
    merchant_id = serializers.IntegerField(write_only=True) # 增加category的时候加的外键id
    goods_list = GoodsSerializer(many=True, read_only=True)
    class Meta:
        model = GoodsCategory
        fields = '__all__'

    # 重写的验证方法
    def validate_merchant_id(self, value):
        if not Merchant.objects.filter(pk=value).exists():
            raise serializers.ValidationError("商家不存在")
        return value

    def create(self, validated_data):
        merchant_id = validated_data.get("merchant_id")
        merchant = Merchant.objects.get(pk=merchant_id)
        category = GoodsCategory.objects.create(**validated_data, merchant=merchant)
        return category