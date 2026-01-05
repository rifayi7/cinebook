from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RifUser
from .serializers import UserSerializer
from django.shortcuts import get_object_or_404




# Create your views here.

class Users(APIView):
    def get(self,request):
        users=RifUser.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response(serializer.data)
    def post(self,request):
        print(request.data)
        serializer= UserSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    

class User(APIView):
    def get(self,request,pk):
        user = get_object_or_404(RifUser, id=pk)
        serializer = UserSerializer(user)
        return Response(serializer.data)