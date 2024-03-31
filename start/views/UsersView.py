from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
import json

from start.models.UsersModel import Users

from start.syntax.UsersSerial import  UserSerializer

class API:
    @api_view(['GET', 'POST'])
    def user(req):
        if req.method == 'GET':
            users = Users.objects.all()
            users_serial = UserSerializer(users, many = True)
            found = True
            resMen = "With Data"

            print(users_serial)
            if not users:
                found = False
                resMen = "Without Data"
                users_serial = None
            return JsonResponse(
                {
                    'Found' : found,
                    'message': resMen, 
                    'content': users_serial.data
                })
        
        # * POST
        if req.method == 'POST':
            user_req = JSONParser().parse(req)
            print(f"""
                    GetData ====> {user_req}
                """)
            user_serial = UserSerializer(data = user_req)
            if user_serial.is_valid():
                user_serial.save()
                return JsonResponse(
                    {
                        "SendDatas" : True,
                    })
            return JsonResponse(
                    {
                        "SendDatas" : False,
                    })
        
    @api_view(['GET', 'POST'])
    def Pass(req):
        if req.method == 'GET':
            pass
