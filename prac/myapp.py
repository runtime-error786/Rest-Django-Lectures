import requests
import json

URL = "http://localhost:8001/stu/"

def get_data(id=None):
    if id is not None:
        params = {"id":id}
        response = requests.get(url=URL,params=params)
        print(response.json())
    else:
        response = requests.get(url=URL)
        print(response.json())
    
get_data(10)
    
def post_data():
    data = {
        'name':'Ab',
        'roll':'998',
        'city':'fsd'
    }
    header = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    request = requests.post(url=URL, headers=header , data=json_data)
    print(request.json())    


# post_data()

def put_data():
    data = {
        'id':9,
        'name':'yar',
        'roll':'9085',
        'city':'lhr'
    }
    header = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    request = requests.put(url=URL, headers=header ,data=json_data)
    print(request.json()) 
    
# put_data()

def patch_data():
    data = {
        'id':9,
        'roll':'9111',
        'city':'krc'
    }
    
    header = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    request = requests.patch(url=URL, headers=header ,data=json_data)
    print(request.json()) 
    
# patch_data()

def delete_data():
    data = {
        'id':9,
    }
    json_data = json.dumps(data)
    
    header = {'content-Type':'application/json'}

    request = requests.delete(url=URL, headers=header ,data=json_data)
    print(request.json()) 
    
# delete_data()
    