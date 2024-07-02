from rest_framework import serializers
from .models import Stu

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
        

class StudentSerializer(serializers.ModelSerializer):
    
    def CheckName(value):
        if value=='mustafa':
            raise serializers.ValidationError("its HR")
        else:
            return value
    class Meta:
        model = Stu
        fields = "__all__"
        # read_only_fields=['name','id']
        # extra_kwargs={'id':{'read_only':True}}
        
    #validator validation
   
    
    # field level validation
    def validate_roll(self,value):
        if value>100:
            raise serializers.ValidationError("roll number is less that 100")
        else:
            return value
        
    # object level validation
    def validate(self, data):
        d1 = data['name']
        d2 = data['roll']
        
        if d1=='mustafa' and d2==9085:
            raise serializers.ValidationError("It's HR")
        else:
            return data
        
    
        
