from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RifUser
from .serializers import UserSerializer



# Create your views here.

class index(APIView):
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
    

# def create_user(request):
#     email = "a2@admin.com"
#     password = "123454546546"
#     username = "admin2"
#     RifUser.objects.create_user(email,password,username=username)
#     return HttpResponse("done")