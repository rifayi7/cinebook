from rest_framework import serializers
from .models import RifUser
from rest_framework.exceptions import ValidationError



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=RifUser
        fields=['email','username', 'password',]
        extra_kwargs = {'password': {'write_only': True}}

    def validate_password(self,value):
        SPECIAL_CHARS = '!@#$%^&*(),.?":{}|<>'
        NUMBERS_COLLECTION = ['0','1','2','3','4','5','6','7','8','9']
        if len(value)<8:
            raise serializers.ValidationError("password should atleast 8 length")
        if not any(char in SPECIAL_CHARS for char in value):
            raise serializers.ValidationError("password must contain atleast a special charcater")
        if not any(char in NUMBERS_COLLECTION for char in value):
            raise serializers.ValidationError("password must contain atleast a number")
        return value



    def create(self, validated_data):
        user = RifUser.objects.create_user(**validated_data,is_active=False)
        return user

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model=RifUser
        fields = ["username","is_active","is_staff","email","is_admin"]
