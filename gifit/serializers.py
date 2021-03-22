from rest_framework import serializers
from rest_framework import serializers
from .models import File
from .models import Roles,Users

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"



class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = "__all__"
