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



from rest_framework.decorators import api_view
from .models import Stu
from .serializers import StudentSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

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
    