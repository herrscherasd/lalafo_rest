from rest_framework import serializers

from apps.users.models import User
from apps.posts.serializer import PostSerializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'phone_number', 'profile_image')

class UserDetailSerializer(serializers.ModelSerializer):
    user_posts = PostSerializer(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'date_joined', 'phone_number', 'profile_image', 'user_posts')

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=100, write_only=True)
    password2 = serializers.CharField(
        max_length=100,write_only=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'phone_number', 'profile_image', 'password', 'password2')
    
    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({'password' : 'Пароли отличаются'})
        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            email = validated_data['email'],
            phone_number = validated_data['phone_number'],
            profile_image = validated_data['profile_image'],
        )
        user.set_password(validated_data['password2'])
        user.save()
        return user