from .models import CustomUser, Company
from rest_framework import serializers
from django.contrib.auth import authenticate


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name']
        extra_kwargs = {'password': {'write_only': True}}

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'name', 'description']

    def create(self, validated_data):
       user = CustomUser.objects.create(**validated_data)
       return user
    
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField()


    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')


        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_active:
                    raise serializers.ValidationError('User account is disabled.')
                attrs['user'] = user
                return attrs
            else:
                raise serializers.ValidationError('Unable to log in with provided credentials.')
        else:
            raise serializers.ValidationError('Must include "email" and "password".')
