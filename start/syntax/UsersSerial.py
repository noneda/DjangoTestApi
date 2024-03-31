from rest_framework import serializers
from ..models.UsersModel import Users
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
                    'name', 
                    'pasw', 
                    'status'
                ]
