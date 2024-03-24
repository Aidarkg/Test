from django.shortcuts import render
from manager.models import Manager
from manager.serializers import ManagerCreateSerializer, ManagerListSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import authenticate, login, logout
from rest_framework.pagination import PageNumberPagination



class ManagerListAPIView(APIView):
    def get(self, request):
        manager = Manager.objects.all()
        serializer = ManagerListSerializer(manager, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ManagerCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(request.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ManagerUpdateDeleteAPIView(APIView):
    def get(self, request, id):
        try:
            manager = Manager.objects.get(id=id)
        except Manager.DoesNotExist:
            return Response({"error": "Менеджер не найден"}, status=status.HTTP_404_NOT_FOUND)
        serializer = ManagerListSerializer(manager).data
        return Response(serializer, status=status.HTTP_200_OK)
    
    def put(self, request, id):
        manager = Manager.objects.get(id=id)
        user = manager.user
        serializer = ManagerListSerializer(data=request.data)
        if serializer.is_valid():
            manager.full_name = request.data.get('full_name')
            manager.phone_number = request.data.get('phone_number')
            user.username = request.data.get('username')
            user.email = request.data.get('email')
            manager.save()
            user.save()
            return Response(data={"message": "Обновление успешно"}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        manager = Manager.objects.get(id=id)
        
        manager.delete()
        return Response({"message": "Удаление успешно"}, status=status.HTTP_200_OK)
    

class LoginAPIView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return Response({"message": "Вход успешно"}, status=status.HTTP_200_OK)
        return Response({"message": "Ошибка входа"}, status=status.HTTP_400_BAD_REQUEST)
    

class LogoutAPIView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Выход успешно"}, status=status.HTTP_200_OK)