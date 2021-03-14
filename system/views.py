import json
import time

from django.http import HttpResponse
from django.shortcuts import render
# from django.views import View
from rest_framework.views import APIView
import user.models as usermodels
from django.utils.decorators import method_decorator
# Create your views here.
def print_time(func):
    def warpper(*args,**kwargs):
        s = time.time()
        func(*args,**kwargs)
        e = time.time()
        print(e-s)
        return func
    return warpper



@method_decorator(print_time,name="post")
class GetRoleName(APIView):
    def post(self,requests):
        sys_objs = usermodels.Role.objects.all().values_list("name")
        print(sys_objs)

        sys_objs = usermodels.Department.objects.all().values_list("department_name")
        print(sys_objs)

        sys_objs = usermodels.User.objects.all().values_list("user_name")
        print(sys_objs)

        sys_objs = usermodels.User.objects.filter(role_id__name="role_1").values_list("user_name")
        print(sys_objs)
        print(sys_objs.query)

        sys_objs = usermodels.User.objects.filter(department_id__department_name="test_b").values_list("user_name")
        print(sys_objs)
        print(sys_objs.query)

        b_id = usermodels.Department.objects.all().department
        print(b_id.all())
        return HttpResponse(json.dumps({"status":"success"}))