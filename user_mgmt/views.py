from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Users, UserTypes, SystemModules, UserTypeModuleMapping
from .serializers import UserSerializer, UserTypeSerializer, SystemModuleSerializer, UserTypeModuleMappingSerializer


class UserListCreateAPIView(APIView):
    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserDetailAPIView(APIView):
    def get_object(self, user_id):
        try:
            return Users.objects.get(user_id=user_id)
        except Users.DoesNotExist:
            raise Http404

    def get(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserSerializer(user)
        return Response(serializer.data)

    def put(self, request, user_id):
        user = self.get_object(user_id)
        serializer = UserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_id):
        user = self.get_object(user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserTypeListCreateAPIView(APIView):
    def get(self, request):
        user_types = UserTypes.objects.all()
        serializer = UserTypeSerializer(user_types, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTypeDetailAPIView(APIView):
    def get_object(self, user_type_id):
        try:
            return UserTypes.objects.get(user_type_id=user_type_id)
        except UserTypes.DoesNotExist:
            raise Http404

    def get(self, request, user_type_id):
        user_type = self.get_object(user_type_id)
        serializer = UserTypeSerializer(user_type)
        return Response(serializer.data)

    def put(self, request, user_type_id):
        user_type = self.get_object(user_type_id)
        serializer = UserTypeSerializer(user_type, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, user_type_id):
        user_type = self.get_object(user_type_id)
        user_type.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class SystemModuleListCreateAPIView(APIView):
    def get(self, request):
        system_modules = SystemModules.objects.all()
        serializer = SystemModuleSerializer(system_modules, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = SystemModuleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SystemModuleDetailAPIView(APIView):
    def get_object(self, system_module_id):
        try:
            return SystemModules.objects.get(system_module_id=system_module_id)
        except SystemModules.DoesNotExist:
            raise Http404

    def get(self, request, system_module_id):
        system_module = self.get_object(system_module_id)
        serializer = SystemModuleSerializer(system_module)
        return Response(serializer.data)

    def put(self, request, system_module_id):
        system_module = self.get_object(system_module_id)
        serializer = SystemModuleSerializer(system_module, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, system_module_id):
        system_module = self.get_object(system_module_id)
        system_module.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserTypeModuleMappingListCreateAPIView(APIView):
    def get(self, request):
        mappings = UserTypeModuleMapping.objects.all()
        serializer = UserTypeModuleMappingSerializer(mappings, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserTypeModuleMappingSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserTypeModuleMappingDetailAPIView(APIView):
    def get_object(self, mapping_id):
        try:
            return UserTypeModuleMapping.objects.get(user_type_module_mapping_id=mapping_id)
        except UserTypeModuleMapping.DoesNotExist:
            raise Http404

    def get(self, request, mapping_id):
        mapping = self.get_object(mapping_id)
        serializer = UserTypeModuleMappingSerializer(mapping)
        return Response(serializer.data)

    def put(self, request, mapping_id):
        mapping = self.get_object(mapping_id)
        serializer = UserTypeModuleMappingSerializer(mapping, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, mapping_id):
        mapping = self.get_object(mapping_id)
        mapping.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
