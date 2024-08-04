from rest_framework import serializers
from django.contrib.auth.models import User
import re

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password', 'password2', 'email']

    def validate(self, data):
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match.")
        if len(data['username']) < 8:
            raise serializers.ValidationError("Username must be at least 8 characters long.")
        if not re.search(r'[a-zA-Z0-9]', data['username']):
            raise serializers.ValidationError("Username must contain alphanumeric characters.")
        
        if not data['email'].endswith('@gmail.com'):
            raise serializers.ValidationError("Email must end with @gmail.com.")
        if not data['password'].isdigit():
            raise serializers.ValidationError("Password must contain only numeric characters.")
        if len(data['password']) < 6:
            raise serializers.ValidationError("Password must be at least 6 characters long.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user
