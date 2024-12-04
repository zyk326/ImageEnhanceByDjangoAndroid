from rest_framework import serializers
from .models import IEUser

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = IEUser
        exclude = ('password', 'user_permissions')

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = IEUser.objects.filter(username=username).first()

            if not user:
                raise serializers.ValidationError("请输入正确的邮箱!")
            if not user.check_password(password):
                raise serializers.ValidationError("请输入正确的密码!")

            attrs['user'] = user
        else:
            raise serializers.ValidationError("请传入用户名和密码!")
        return attrs

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = IEUser
        fields = ['username', 'password']  # 需要的字段

    def create(self, validated_data):
        user = IEUser.objects.create_user(**validated_data)  # 使用自定义的 create_user 方法
        return user