# 1.用来序列化
# 2.用来验证表单数据
# 3.可以创建数据,修改数据

# form -> serializer
from rest_framework import serializers
from meituan.models import Merchant, GoodsCategory


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