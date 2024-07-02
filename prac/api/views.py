from .models import Stu
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def Student_View(req):
    if req.method == "GET":
        try:
            id = req.GET.get("id")
            if id is not None:
                print("Received ID:", id)  # Debug print
                db_data = Stu.objects.get(id=id)
                print("Database Data:", db_data)  # Debug print
                serialize_data = StudentSerializer(db_data)
                json_data = JSONRenderer().render(serialize_data.data)
                return HttpResponse(json_data, content_type="application/json")
            else:
                db_data = Stu.objects.all()
                serialize_data = StudentSerializer(db_data,many=True)
                json_data = JSONRenderer().render(serialize_data.data)
                return HttpResponse(json_data, content_type="application/json")
        except ObjectDoesNotExist:
            return HttpResponse(
                '{"msg": "Data not found"}',
                content_type="application/json",
                status=404
            )
        except Exception as e:
            return HttpResponse(
                '{"msg": "Server error"}',
                content_type="application/json",
                status=500
            )
    elif req.method=="POST":
        try:
            json_str = req.body.decode('utf-8')  # Decode bytes to UTF-8 string
            print(json_str)
            data = json.loads(json_str)  
            serialize_data = StudentSerializer(data=data)
            print("ssssssssssss")
            if serialize_data.is_valid():
                print("ssssssssssssssskkkkk")
                serialize_data.save()
                return HttpResponse(
                '{"msg": "data saved"}',
                content_type="application/json",
                status=404
            )
            else:
                return HttpResponse(
                '{"msg": "Data not inserted"}',
                content_type="application/json",
                status=404
            )
          
        except Exception as e:
            return HttpResponse(
                '{"msg": "Server error"}',
                content_type="application/json",
                status=500
            )
    elif req.method=="PUT":
        try:
            json_str = req.body.decode('utf-8') 
            print(json_str)
            data = json.loads(json_str) 
            print(data)
            db_data = Stu.objects.get(id=data['id']) 
            serialize_data = StudentSerializer(db_data , data=data)
           
            if serialize_data.is_valid():
                print("here is line run")
                serialize_data.save()
                return HttpResponse(
                '{"msg": "data Update"}',
                content_type="application/json",
                status=404
            )
            else:
                return HttpResponse(
                '{"msg": "Data not Update"}',
                content_type="application/json",
                status=404
            )
        except Exception as e:
            return HttpResponse(
                '{"msg": "Server error"}',
                content_type="application/json",
                status=500
            )
    elif req.method=="PATCH":
        try:
            json_str = req.body.decode('utf-8') 
            print(json_str)
            data = json.loads(json_str) 
            print(data)
            db_data = Stu.objects.get(id=data['id']) 
            serialize_data = StudentSerializer(db_data , data=data, partial=True)
            if serialize_data.is_valid():
                serialize_data.save()
                return HttpResponse(
                '{"msg": "data Update"}',
                content_type="application/json",
                status=404
            )
            else:
                return HttpResponse(
                '{"msg": "Data not Update"}',
                content_type="application/json",
                status=404
            )
        except Exception as e:
            return HttpResponse(
                '{"msg": "Server error"}',
                content_type="application/json",
                status=500
            )
    elif req.method=="DELETE":
        try:
            json_str = req.body.decode('utf-8') 
            print(json_str)
            data = json.loads(json_str) 
            print(data)
            db_data = Stu.objects.get(id=data['id']) 
            db_data.delete()
            return HttpResponse(
                '{"msg": "data deleted"}',
                content_type="application/json",
                status=500
            )
        except Exception as e:
            return HttpResponse(
                '{"msg": "Server error"}',
                content_type="application/json",
                status=500
            )
