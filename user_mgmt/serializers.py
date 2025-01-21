from rest_framework import serializers
from .models import Users, UserTypes, SystemModules, UserTypeModuleMapping

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = '__all__'


class UserTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTypes
        fields = '__all__'


class SystemModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystemModules
        fields = '__all__'


class UserTypeModuleMappingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTypeModuleMapping
        fields = '__all__'
