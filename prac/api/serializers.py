# from rest_framework import serializers
# from .models import Stu

# class StudentSerializer(serializers.Serializer):
          
#     #validator validation
#     def CheckName(value):
#         if value=='mustafa':
#             raise serializers.ValidationError("its HR")
#         else:
#             return value
        
#     id = serializers.IntegerField(read_only=True,validators=[CheckName])
#     name = serializers.CharField(max_length=200)
#     roll = serializers.IntegerField()
#     city = serializers.CharField(max_length=100)
    
    
#     def create(self,validate_data):
#         return Stu.objects.create(**validate_data)
    
    
#     def update(self,instance,validate_data):
#         instance.name = validate_data.get('name',instance.name)
#         instance.roll = validate_data.get('roll',instance.roll)
#         instance.city = validate_data.get('city',instance.city)
#         instance.save()
#         return instance
    
#     # field level validation
#     def validate_roll(self,value):
#         if value>100:
#             raise serializers.ValidationError("roll number is less that 100")
#         else:
#             return value
        
#     # object level validation
#     def validate(self, data):
#         d1 = data['name']
#         d2 = data['roll']
        
#         if d1=='mustafa' and d2==9085:
#             raise serializers.ValidationError("It's HR")
#         else:
#             return data
        
#     #validator validation
#     def CheckName(value):
#         if value=='mustafa':
#             raise serializers.ValidationError("its HR")
#         else:
#             return value
        

# class StudentSerializer(serializers.ModelSerializer):
    
#     def CheckName(value):
#         if value=='mustafa':
#             raise serializers.ValidationError("its HR")
#         else:
#             return value
#     class Meta:
#         model = Stu
#         fields = "__all__"
#         # read_only_fields=['name','id']
#         # extra_kwargs={'id':{'read_only':True}}
        
#     #validator validation
   
    
#     # field level validation
#     def validate_roll(self,value):
#         if value>100:
#             raise serializers.ValidationError("roll number is less that 100")
#         else:
#             return value
        
#     # object level validation
#     def validate(self, data):
#         d1 = data['name']
#         d2 = data['roll']
        
#         if d1=='mustafa' and d2==9085:
#             raise serializers.ValidationError("It's HR")
#         else:
#             return data
        
    
# class StudentSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Stu
#         fields = "__all__"
       
       
       
       # serializers.py
# serializers.py

from rest_framework import serializers
from .models import CustomUser
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.exceptions import AuthenticationFailed
from django.contrib.auth.hashers import make_password, check_password

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('email', 'first_name', 'last_name', 'phone_no', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email=validated_data['email'],
            first_name=validated_data.get('first_name', ''),
            last_name=validated_data.get('last_name', ''),
            phone_no=validated_data.get('phone_no', ''),
            password=validated_data['password']
        )
        return user

import logging

logger = logging.getLogger(__name__)


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = CustomUser.USERNAME_FIELD

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token[cls.username_field] = getattr(user, cls.username_field)
        token['first_name'] = user.first_name
        token['last_name'] = user.last_name
        token['phone_no'] = user.phone_no
        return token

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            try:
                user = CustomUser.objects.get(email=email)
            except CustomUser.DoesNotExist:
                raise AuthenticationFailed("User not found.")
            
            if not user.is_active:
                raise AuthenticationFailed("User account is not active.")
            
            if not user.check_password(password):
                raise AuthenticationFailed("Incorrect password.")

            token = self.get_token(user)
            return {
                'access': str(token.access_token),
                'refresh': str(token),
            }
          
        else:
            raise AuthenticationFailed("Must include 'email' and 'password'.")
        
from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        refresh = attrs.get('refresh')

        if refresh:
            try:
                refresh_token = RefreshToken(refresh)
                data = {'access': str(refresh_token.access_token)}
            except TokenError:
                raise InvalidToken('Token is invalid or expired')
            
            return data

        raise InvalidToken('No valid token provided')