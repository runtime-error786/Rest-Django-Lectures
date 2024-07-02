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
    
# get_data()
    
def post_data():
    data = {
        'name':'Abdullah',
        'roll':'88',
        'city':'fsd'
    }
    json_data = json.dumps(data)
    request = requests.post(url=URL,data=json_data)
    print(request.json())    


# post_data()

def put_data():
    data = {
        'id':9,
        'name':'mustafa',
        'roll':'89',
        'city':'fsd'
    }
    json_data = json.dumps(data)
    request = requests.put(url=URL,data=json_data)
    print(request.json()) 
    
put_data()

def patch_data():
    data = {
        'id':2,
        'name':'musu',
        'roll':'9111',
        'city':'krc'
    }
    json_data = json.dumps(data)
    request = requests.patch(url=URL,data=json_data)
    print(request.json()) 
    
# patch_data()

def delete_data():
    data = {
        'id':1,
    }
    json_data = json.dumps(data)
    request = requests.delete(url=URL,data=json_data)
    print(request.json()) 
    
# delete_data()
    