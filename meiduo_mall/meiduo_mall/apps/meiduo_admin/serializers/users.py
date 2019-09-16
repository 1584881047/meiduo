from django.utils import timezone
from rest_framework import serializers

from users.models import User


class AdminAuthSerializer(serializers.ModelSerializer):
    username = serializers.CharField(label='用户名')
    token = serializers.CharField(label='JWT Token', read_only=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'token')
        extra_kwargs = {
            'password': {
                'write_only': True
            }

        }

    def validate(self, attrs):
        username = attrs['username']
        password = attrs['password']

        try:
            user = User.objects.get(username=username, is_staff=True)
        except User.DoesNotExist as e:
            raise serializers.ValidationError('用户名或密码错误')

        if not user.check_password(password):
            raise serializers.ValidationError('用户名或密码错误')

        attrs['user'] = user

        return attrs

    def create(self, validated_data):
        user = validated_data['user']
        from rest_framework_jwt.settings import api_settings

        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        # 更新最后登录时间
        user.last_login = timezone.now()
        user.save()

        user.token = token

        return user


class UserSerializer(serializers.ModelSerializer):
    """用户序列化器类"""

    class Meta:
        model = User
        fields = ('id', 'username', 'mobile', 'email')
