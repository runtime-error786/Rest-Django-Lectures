from rest_framework.permissions import BasePermission

class Custome_Permission(BasePermission):
    def has_permission(self,request,view):
        if request.method=="GET":
            return True
        else:
            return False
