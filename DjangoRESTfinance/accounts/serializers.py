from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


UserModel = get_user_model()

class RegisterUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = UserModel
        fields = ['email', 'username', 'password']

    def create(self, validated_data):
        user = UserModel.objects.create_user( # create_user() to hash the password
            email=validated_data['email'],
            username=validated_data['username'],
            password=validated_data['password'],
        )
        return user

class EmailOrUsernameTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'username'  # required for JWT logic

    def validate(self, attrs):
        login_value = attrs.get('username') or attrs.get('email')
        password = attrs.get('password')
        user = None

        # Try to get user by email first
        if login_value:
            try:
                user = UserModel.objects.get(email=login_value)
            except UserModel.DoesNotExist:
                # Try username
                try:
                    user = UserModel.objects.get(username=login_value)
                except UserModel.DoesNotExist:
                    pass

        if user and user.check_password(password) and user.is_active:
            attrs['user'] = user
            return super().validate(attrs)
        raise serializers.ValidationError("No active account found with the given credentials")

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()
