from rest_framework import serializers
from django.core.validators import FileExtensionValidator

class UploadImageSerializer(serializers.Serializer):
    image = serializers.ImageField(
        # validators=[FileExtensionValidator(get_available_image_extensions())]
        validators = [FileExtensionValidator(allowed_extensions=['png', 'jpg', 'jpeg'])],
        error_messages = {'required': '请上传图片!', 'invalid_image':'请上传正确格式的图片!'}
    )

    def validate_image(self, value):
        max_size = 10 * 1024 * 1024
        size = value.size
        if size > max_size:
            raise serializers.ValidationError('图片最大不能超过10MB!')
        return value