# from .models import Stu
# from .serializers import StudentSerializer
# from rest_framework.renderers import JSONRenderer
# from django.http import HttpResponse
# from django.core.exceptions import ObjectDoesNotExist
# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# import json

# @csrf_exempt
# def Student_View(req):
#     if req.method == "GET":
#         try:
#             id = req.GET.get("id")
#             if id is not None:
#                 print("Received ID:", id)  # Debug print
#                 db_data = Stu.objects.get(id=id)
#                 print("Database Data:", db_data)  # Debug print
#                 serialize_data = StudentSerializer(db_data)
#                 json_data = JSONRenderer().render(serialize_data.data)
#                 return HttpResponse(json_data, content_type="application/json")
#             else:
#                 db_data = Stu.objects.all()
#                 serialize_data = StudentSerializer(db_data,many=True)
#                 json_data = JSONRenderer().render(serialize_data.data)
#                 return HttpResponse(json_data, content_type="application/json")
#         except ObjectDoesNotExist:
#             return HttpResponse(
#                 '{"msg": "Data not found"}',
#                 content_type="application/json",
#                 status=404
#             )
#         except Exception as e:
#             return HttpResponse(
#                 '{"msg": "Server error"}',
#                 content_type="application/json",
#                 status=500
#             )
#     elif req.method=="POST":
#         try:
#             json_str = req.body.decode('utf-8')  # Decode bytes to UTF-8 string
#             print(json_str)
#             data = json.loads(json_str)  
#             serialize_data = StudentSerializer(data=data)
#             print("ssssssssssss")
#             if serialize_data.is_valid():
#                 print("ssssssssssssssskkkkk")
#                 serialize_data.save()
#                 return HttpResponse(
#                 '{"msg": "data saved"}',
#                 content_type="application/json",
#                 status=404
#             )
#             else:
#                 return HttpResponse(
#                 '{"msg": "Data not inserted"}',
#                 content_type="application/json",
#                 status=404
#             )
          
#         except Exception as e:
#             return HttpResponse(
#                 '{"msg": "Server error"}',
#                 content_type="application/json",
#                 status=500
#             )
#     elif req.method=="PUT":
#         try:
#             json_str = req.body.decode('utf-8') 
#             print(json_str)
#             data = json.loads(json_str) 
#             print(data)
#             db_data = Stu.objects.get(id=data['id']) 
#             serialize_data = StudentSerializer(db_data , data=data)
           
#             if serialize_data.is_valid():
#                 print("here is line run")
#                 serialize_data.save()
#                 return HttpResponse(
#                 '{"msg": "data Update"}',
#                 content_type="application/json",
#                 status=404
#             )
#             else:
#                 return HttpResponse(
#                 '{"msg": "Data not Update"}',
#                 content_type="application/json",
#                 status=404
#             )
#         except Exception as e:
#             return HttpResponse(
#                 '{"msg": "Server error"}',
#                 content_type="application/json",
#                 status=500
#             )
#     elif req.method=="PATCH":
#         try:
#             json_str = req.body.decode('utf-8') 
#             print(json_str)
#             data = json.loads(json_str) 
#             print(data)
#             db_data = Stu.objects.get(id=data['id']) 
#             serialize_data = StudentSerializer(db_data , data=data, partial=True)
#             if serialize_data.is_valid():
#                 serialize_data.save()
#                 return HttpResponse(
#                 '{"msg": "data Update"}',
#                 content_type="application/json",
#                 status=404
#             )
#             else:
#                 return HttpResponse(
#                 '{"msg": "Data not Update"}',
#                 content_type="application/json",
#                 status=404
#             )
#         except Exception as e:
#             return HttpResponse(
#                 '{"msg": "Server error"}',
#                 content_type="application/json",
#                 status=500
#             )
#     elif req.method=="DELETE":
#         try:
#             json_str = req.body.decode('utf-8') 
#             print(json_str)
#             data = json.loads(json_str) 
#             print(data)
#             db_data = Stu.objects.get(id=data['id']) 
#             db_data.delete()
#             return HttpResponse(
#                 '{"msg": "data deleted"}',
#                 content_type="application/json",
#                 status=500
#             )
#         except Exception as e:
#             return HttpResponse(
#                 '{"msg": "Server error"}',
#                 content_type="application/json",
#                 status=500
#             )



# from rest_framework.decorators import api_view
# from .models import Stu
# from .serializers import StudentSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView

# @api_view(["GET","POST","PUT","PATCH","DELETE"])
# def Student_View(req):
#     if req.method == "GET":
#             id = req.GET.get("id")
#             if id is not None:
#                 print("Received ID:", id)  # Debug print
#                 db_data = Stu.objects.get(id=id)
#                 print("Database Data:", db_data)  # Debug print
#                 serialize_data = StudentSerializer(db_data)
#                 return Response(data=serialize_data.data, status=status.HTTP_200_OK)
#             else:
#                 db_data = Stu.objects.all()
#                 serialize_data = StudentSerializer(db_data,many=True)
#                 return Response(data=serialize_data.data, status=status.HTTP_404_NOT_FOUND)
#     elif req.method=="POST":
#             data = req.data 
#             serialize_data = StudentSerializer(data=data)
#             print("ssssssssssss")
#             if serialize_data.is_valid():
#                 print("ssssssssssssssskkkkk")
#                 serialize_data.save()
#                 return Response(data={'msg':'data is posted'}, status=status.HTTP_200_OK)
#             else:
#                  return Response(data={'msg':'data is not posted'}, status=status.HTTP_404_NOT_FOUND)
#     elif req.method=="PUT":
#             data = req.data 
#             db_data = Stu.objects.get(id=data['id']) 
#             serialize_data = StudentSerializer(db_data , data=data)
#             if serialize_data.is_valid():
#                 print("here is line run")
#                 serialize_data.save()
#                 return Response(data={'msg':'data is updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(data={'msg':'data is not  posted'}, status=status.HTTP_404_NOT_FOUND)
        
#     elif req.method=="PATCH":
#             data = req.data 
#             db_data = Stu.objects.get(id=data['id']) 
#             serialize_data = StudentSerializer(db_data , data=data, partial=True)
#             if serialize_data.is_valid():
#                 serialize_data.save()
#                 return Response(data={'msg':'data  patch updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(data={'msg':'data  patch not updated'}, status=status.HTTP_404_NOT_FOUND)
       
#     elif req.method=="DELETE":
#             data = req.data 
#             db_data = Stu.objects.get(id=data['id']) 
#             db_data.delete()
#             return Response(data={'msg':'data is deleted'}, status=status.HTTP_200_OK)

        

# class Student_View(APIView):
#     def get(self,req,pk=None,format=None):
#             id = pk
#             if id is not None:
#                 print("Received ID:", id)  # Debug print
#                 db_data = Stu.objects.get(id=id)
#                 print("Database Data:", db_data)  # Debug print
#                 serialize_data = StudentSerializer(db_data)
#                 return Response(data=serialize_data.data, status=status.HTTP_200_OK)
#             else:
#                 db_data = Stu.objects.all()
#                 serialize_data = StudentSerializer(db_data,many=True)
#                 return Response(data=serialize_data.data, status=status.HTTP_404_NOT_FOUND)
            
#     def post(self,request,format=None):
#             data = request.data 
#             print(data)
#             serialize_data = StudentSerializer(data=data)
#             print("ssssssssssss")
#             if serialize_data.is_valid():
#                 print("ssssssssssssssskkkkk")
#                 serialize_data.save()
#                 return Response(data={'msg':'data is posted'}, status=status.HTTP_200_OK)
#             else:
#                  return Response(data={'msg':'data is not posted'}, status=status.HTTP_404_NOT_FOUND)
             
             
#     def put(self,request,pk=None,format=None):
#             data = request.data 
#             db_data = Stu.objects.get(id=pk) 
#             serialize_data = StudentSerializer(db_data , data=data)
#             if serialize_data.is_valid():
#                 print("here is line run")
#                 serialize_data.save()
#                 return Response(data={'msg':'data is updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(data={'msg':'data is not  posted'}, status=status.HTTP_404_NOT_FOUND)
            
#     def patch(self,request,pk=None,format=None):
#             data = request.data 
#             db_data = Stu.objects.get(id=pk) 
#             serialize_data = StudentSerializer(db_data , data=data, partial=True)
#             if serialize_data.is_valid():
#                 serialize_data.save()
#                 return Response(data={'msg':'data  patch updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(data={'msg':'data  patch not updated'}, status=status.HTTP_404_NOT_FOUND)
            
#     def delete(self,request,pk=None,format=None):
#             data = request.data 
#             db_data = Stu.objects.get(id=pk) 
#             db_data.delete()
#             return Response(data={'msg':'data is deleted'}, status=status.HTTP_200_OK)
            
# from rest_framework.generics import GenericAPIView
# from rest_framework.mixins import ListModelMixin,CreateModelMixin,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin

# # pk not required
# class Student_View(GenericAPIView,ListModelMixin,CreateModelMixin):
#     queryset = Stu.objects.all()
#     serializer_class = StudentSerializer
    
#     def get(self,request,*args,**kwargs):
#         return self.list(request,*args,**kwargs)
    
#     def post(self,request,*args,**kwargs):
#         return self.create(request,*args,**kwargs)
    
    

# # pk required
# class Student_View1(GenericAPIView,UpdateModelMixin,DestroyModelMixin,RetrieveModelMixin):
#     queryset = Stu.objects.all()
#     serializer_class = StudentSerializer
    
#     def put(self,request,*args,**kwargs):
#         return self.update(request,*args,**kwargs)
    
#     def get(self,request,*args,**kwargs):
#         return self.retrieve(request,*args,**kwargs)
    
#     def delete(self,request,*args,**kwargs):
#         return self.destroy(request,*args,**kwargs)

# from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveDestroyAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView,DestroyAPIView
# # generic is class base
# class Student_View(RetrieveDestroyAPIView):
#     queryset = Stu.objects.all()
#     serializer_class = StudentSerializer

# from rest_framework import viewsets
 
# class Student_View(viewsets.ViewSet):
#     def list(self,request):
#         db_data = Stu.objects.all()
#         serialize_data = StudentSerializer(db_data,many=True)
#         return Response(data=serialize_data.data, status=status.HTTP_404_NOT_FOUND)
            
#     def create(self,request):
#             data = request.data 
#             print(data)
#             serialize_data = StudentSerializer(data=data)
#             print("ssssssssssss")
#             if serialize_data.is_valid():
#                 print("ssssssssssssssskkkkk")
#                 serialize_data.save()
#                 return Response(data={'msg':'data is posted'}, status=status.HTTP_200_OK)
#             else:
#                  return Response(data={'msg':'data is not posted'}, status=status.HTTP_404_NOT_FOUND)
             
             
#     def update(self,request,pk=None):
#             data = request.data 
#             db_data = Stu.objects.get(id=pk) 
#             serialize_data = StudentSerializer(db_data , data=data)
#             if serialize_data.is_valid():
#                 print("here is line run")
#                 serialize_data.save()
#                 return Response(data={'msg':'data is updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(data={'msg':'data is not  posted'}, status=status.HTTP_404_NOT_FOUND)
    
#     def retrieve(self,request,pk=None):
#             id = pk
#             print("Received ID:", id)  # Debug print
#             db_data = Stu.objects.get(id=id)
#             print("Database Data:", db_data)  # Debug print
#             serialize_data = StudentSerializer(db_data)
#             return Response(data=serialize_data.data, status=status.HTTP_200_OK)
            
            
#     def partial_update(self,request,pk=None):
#             data = request.data 
#             db_data = Stu.objects.get(id=pk) 
#             serialize_data = StudentSerializer(db_data , data=data, partial=True)
#             if serialize_data.is_valid():
#                 serialize_data.save()
#                 return Response(data={'msg':'data  patch updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(data={'msg':'data  patch not updated'}, status=status.HTTP_404_NOT_FOUND)
            
#     def destroy(self,request,pk=None):
#             data = request.data 
#             db_data = Stu.objects.get(id=pk) 
#             db_data.delete()
#             return Response(data={'msg':'data is deleted'}, status=status.HTTP_200_OK)


# from rest_framework import viewsets
# class Student_View(viewsets.ModelViewSet):
#     queryset = Stu.objects.all()
#     serializer_class = StudentSerializer
    
    
# from rest_framework import viewsets
# class Student_View(viewsets.ReadOnlyModelViewSet):
#     queryset = Stu.objects.all()
#     serializer_class = StudentSerializer


# from rest_framework import viewsets
# from rest_framework.authentication import BasicAuthentication,SessionAuthentication
# from rest_framework.permissions import IsAuthenticated,IsAdminUser,AllowAny,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
# from .Custome_permission import Custome_Permission
# class Student_View(viewsets.ModelViewSet):
#     queryset = Stu.objects.all()
#     serializer_class = StudentSerializer
#     # authentication_classes=[BasicAuthentication]
#     authentication_classes = [SessionAuthentication]
#     permission_classes=[Custome_Permission]


# from rest_framework.decorators import permission_classes,authentication_classes
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.decorators import api_view
# from .models import Stu
# from .serializers import StudentSerializer
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView

# @api_view(["GET","POST","PUT","PATCH","DELETE"])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
# def Student_View(req):
#     if req.method == "GET":
#             id = req.GET.get("id")
#             if id is not None:
#                 print("Received ID:", id)  # Debug print
#                 db_data = Stu.objects.get(id=id)
#                 print("Database Data:", db_data)  # Debug print
#                 serialize_data = StudentSerializer(db_data)
#                 return Response(data=serialize_data.data, status=status.HTTP_200_OK)
#             else:
#                 db_data = Stu.objects.all()
#                 serialize_data = StudentSerializer(db_data,many=True)
#                 return Response(data=serialize_data.data, status=status.HTTP_404_NOT_FOUND)
#     elif req.method=="POST":
#             data = req.data 
#             serialize_data = StudentSerializer(data=data)
#             print("ssssssssssss")
#             if serialize_data.is_valid():
#                 print("ssssssssssssssskkkkk")
#                 serialize_data.save()
#                 return Response(data={'msg':'data is posted'}, status=status.HTTP_200_OK)
#             else:
#                  return Response(data={'msg':'data is not posted'}, status=status.HTTP_404_NOT_FOUND)
#     elif req.method=="PUT":
#             data = req.data 
#             db_data = Stu.objects.get(id=data['id']) 
#             serialize_data = StudentSerializer(db_data , data=data)
#             if serialize_data.is_valid():
#                 print("here is line run")
#                 serialize_data.save()
#                 return Response(data={'msg':'data is updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(data={'msg':'data is not  posted'}, status=status.HTTP_404_NOT_FOUND)
        
#     elif req.method=="PATCH":
#             data = req.data 
#             db_data = Stu.objects.get(id=data['id']) 
#             serialize_data = StudentSerializer(db_data , data=data, partial=True)
#             if serialize_data.is_valid():
#                 serialize_data.save()
#                 return Response(data={'msg':'data  patch updated'}, status=status.HTTP_200_OK)
#             else:
#                 return Response(data={'msg':'data  patch not updated'}, status=status.HTTP_404_NOT_FOUND)
       
#     elif req.method=="DELETE":
#             data = req.data 
#             db_data = Stu.objects.get(id=data['id']) 
#             db_data.delete()
#             return Response(data={'msg':'data is deleted'}, status=status.HTTP_200_OK)


# views.py
# from rest_framework import generics
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import CustomUser
# from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
# from rest_framework import viewsets
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticated

# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[IsAuthenticated]
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
    
# from rest_framework_simplejwt.views import TokenRefreshView
# from .serializers import CustomTokenRefreshSerializer

# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer

# from rest_framework import generics
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import CustomUser
# from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
# from rest_framework import viewsets
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     throttle_classes = [AnonRateThrottle,UserRateThrottle]
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
    
# from rest_framework_simplejwt.views import TokenRefreshView
# from .serializers import CustomTokenRefreshSerializer

# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer



# from rest_framework import generics
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import CustomUser
# from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
# from rest_framework import viewsets
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
# from .throttle import MustafaThrottle

# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     throttle_classes = [AnonRateThrottle,MustafaThrottle]
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
    
# from rest_framework_simplejwt.views import TokenRefreshView
# from .serializers import CustomTokenRefreshSerializer

# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer

# from rest_framework import generics
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import CustomUser
# from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
# from rest_framework import viewsets
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
# from .throttle import MustafaThrottle

# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     authentication_classes=[JWTAuthentication]
#     permission_classes=[IsAuthenticatedOrReadOnly]
#     throttle_classes = [AnonRateThrottle,ScopedRateThrottle]
#     throttle_scope='viewstu'
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
    
# from rest_framework_simplejwt.views import TokenRefreshView
# from .serializers import CustomTokenRefreshSerializer

# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer

# from rest_framework import generics
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import CustomUser
# from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
# from rest_framework import viewsets
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
# from .throttle import MustafaThrottle
# from rest_framework.authentication import BasicAuthentication

# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     authentication_classes=[BasicAuthentication]
#     permission_classes=[IsAuthenticated]
#     def get_queryset(self):
#         user = self.request.user
#         if user.is_anonymous:
#             return CustomUser.objects.none()  # or handle appropriately
#         return CustomUser.objects.filter(email=user.email)
    
# from rest_framework_simplejwt.views import TokenRefreshView
# from .serializers import CustomTokenRefreshSerializer

# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer

# from rest_framework import generics
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import CustomUser
# from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
# from rest_framework import viewsets
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
# from .throttle import MustafaThrottle
# from rest_framework.authentication import BasicAuthentication

# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     filterset_fields = ['email']
    
    
    
# from rest_framework_simplejwt.views import TokenRefreshView
# from .serializers import CustomTokenRefreshSerializer

# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer

# from rest_framework import generics
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import CustomUser
# from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
# from rest_framework import viewsets
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
# from .throttle import MustafaThrottle
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.filters import SearchFilter

# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     filter_backends=[SearchFilter]
#     search_fields = ['email',"first_name"]
#     # search_fields = ['^email']
#     # search_fields = ['=email']
    
    
    
# from rest_framework_simplejwt.views import TokenRefreshView
# from .serializers import CustomTokenRefreshSerializer

# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer


# from rest_framework import generics
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import CustomUser
# from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
# from rest_framework import viewsets
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
# from .throttle import MustafaThrottle
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.filters import OrderingFilter
# from .page import MY_page
# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     filter_backends=[OrderingFilter]
#     ordering_fields=['first_name']
    
    
    
# from rest_framework_simplejwt.views import TokenRefreshView
# from .serializers import CustomTokenRefreshSerializer

# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer


# from rest_framework import generics
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import CustomUser
# from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
# from rest_framework import viewsets
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
# from .throttle import MustafaThrottle
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.filters import OrderingFilter
# from .page import MY_page
# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     pagination_class = MY_page
    
    
    
# from rest_framework_simplejwt.views import TokenRefreshView
# from .serializers import CustomTokenRefreshSerializer

# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer


# from rest_framework import generics
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .models import CustomUser
# from .serializers import CustomUserSerializer, CustomTokenObtainPairSerializer
# from rest_framework import viewsets
# from rest_framework_simplejwt.authentication import JWTAuthentication
# from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated
# from rest_framework.throttling import AnonRateThrottle,UserRateThrottle,ScopedRateThrottle
# from .throttle import MustafaThrottle
# from rest_framework.authentication import BasicAuthentication
# from rest_framework.filters import OrderingFilter
# from .page import MY_page
# class RegisterView(generics.CreateAPIView):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer

# class CustomTokenObtainPairView(TokenObtainPairView):
#     serializer_class = CustomTokenObtainPairSerializer

# class CustomUserViewSet(viewsets.ModelViewSet):
#     queryset = CustomUser.objects.all()
#     serializer_class = CustomUserSerializer
#     pagination_class = MY_page
    
    
    
# from rest_framework_simplejwt.views import TokenRefreshView
# from .serializers import CustomTokenRefreshSerializer

# class CustomTokenRefreshView(TokenRefreshView):
#     serializer_class = CustomTokenRefreshSerializer


from .models import Singer,Song

from rest_framework import viewsets
from .serializers import SingerSerializer,SongSerializer

class SingView(viewsets.ModelViewSet):
    queryset = Singer.objects.all()
    serializer_class = SingerSerializer
    
class SongView(viewsets.ModelViewSet):
    queryset = Song.objects.all()
    serializer_class = SongSerializer