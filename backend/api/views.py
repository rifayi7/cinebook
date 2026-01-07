from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import RifUser
from .serializers import UserSerializer,AdminUserSerializer
from rest_framework import status


# utils/email.py
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.conf import settings
from .tokens import account_activation_token
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

def send_activation_email(user, request):
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    token = account_activation_token.make_token(user)

    activation_link = request.build_absolute_uri(
        reverse('activate-account', kwargs={
            'uidb64': uid,
            'token': token
        })
    )

    subject = "Activate your account"
    message = f"""
Hello {user.username},

Click the link below to activate your account:
{activation_link}

If you didn't request this, ignore this email.
"""

    email = EmailMessage(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email]
    )
    email.send()

class ActivateAccount(APIView):
    def get(self, request, uidb64, token):
        try:
            uid = force_str(urlsafe_base64_decode(uidb64))
            user = RifUser.objects.get(pk=uid)
        except (TypeError, ValueError, OverflowError, RifUser.DoesNotExist):
            return Response(
                {"message": "Invalid activation link"},
                status=status.HTTP_400_BAD_REQUEST
            )

        if account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return Response(
                {"message": "Account activated successfully"},
                status=status.HTTP_200_OK
            )

        return Response(
            {"message": "Activation link expired or invalid"},
            status=status.HTTP_400_BAD_REQUEST
        )



class Users(APIView):
    def get(self,request):
        users=RifUser.objects.all()
        serializer=UserSerializer(users,many=True)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)
    def post(self,request):
        serializer= UserSerializer(data = request.data)

        if serializer.is_valid():
            user = serializer.save()
            send_activation_email(user, request)
            
            return Response(
                {
                    "message": "User created. Check email to activate account."
                },
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
    

class User(APIView):
    def get(self,request,pk):
        try:
            user = RifUser.objects.get(id=pk)
        except RifUser.DoesNotExist:
            return Response({"message":"user does not exist"},status =status.HTTP_404_NOT_FOUND)
        serializer = UserSerializer(user)
        return Response({"data":serializer.data},status=status.HTTP_200_OK)
    



class SingleUserListForAdmin(APIView):
    def get(self,request,pk):
        user = RifUser.objects.get(id=pk)
        serializer = AdminUserSerializer(user)
        return Response(serializer.data)
    def put(self,request,pk):
        try:
            user = RifUser.objects.get(id=pk)
        except RifUser.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)
        serializer = AdminUserSerializer(user,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=200)
        return Response(serializer.errors, status=400)
    def patch(self, request, pk):
        try:
            user = RifUser.objects.get(id=pk)
        except RifUser.DoesNotExist:
            return Response({"detail": "User not found"}, status=404)

        serializer = AdminUserSerializer(user, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)

        return Response(serializer.errors, status=400)
class UserListForAdmin(APIView):
    def get(self,request):
        users = RifUser.objects.all()
        serializer = AdminUserSerializer(users,many=True)
        return Response(serializer.data)
    