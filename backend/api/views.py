from django.shortcuts import render
from .models import UserData , EventModel , EventReg , Participants , DigitalCertificate
from .serializers import UserDataSerializer , EventModelSerializer , EventRegSerializer , ParticipantsSerializer, DigitalCertificateSerializer , LoginSerializer

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

from django.contrib.auth import authenticate , login , logout
from django.views.decorators.csrf import csrf_exempt


class UserDataAPI(APIView):
    def get(self,request):
        queryset = UserData.objects.all()
        serializer = UserDataSerializer(queryset , many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = UserDataSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
 

@api_view(["POST"])       
def user_login(request):
      data = request.data 
      email = data["email"]
      password = data["password"]
      
      user = authenticate(email=email,password=password)
      if user is not None:
          login(request , user)
          return Response({"message":"Login Successfully"},status=status.HTTP_200_OK)
      else:
          return Response({"error":"Invalid Credintials"},status=status.HTTP_400_BAD_REQUEST)
      