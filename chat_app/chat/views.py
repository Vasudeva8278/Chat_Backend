from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ChatRoom,Message
from rest_framework import status
from .serializer import ChatRoomSerializer,MessageSerializer,LoginSerializer
from rest_framework.authtoken.models import Token
from rest_framework import viewsets

# Create your views here.

def home(request):
    return HttpResponse("welcome chat application")


class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset  = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer


class LoginApiview(APIView):
    def post(self,request,*args,**kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        username = serializer.validated_data['username']
        password = serializer.validated_data['password']

        user = authenticate(username=username,password=password)

        if user is not None:
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token':token.key},status=status.HTTP_200_OK)
        else:
            return Response({"error:'Invalid credentials"},status=status.HTTP_400_BAD_REQUEST)