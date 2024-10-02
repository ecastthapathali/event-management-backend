from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken  
from .models import UserData , EventModel , EventReg , Participants , DigitalCertificate
from .serializers import UserDataSerializer, LoginSerializer , EventModelSerializer , EventRegSerializer , ParticipantsSerializer, DigitalCertificateSerializer
from rest_framework.permissions import AllowAny

class UserDataRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

class UserDataListCreateAPI(generics.ListCreateAPIView):
    queryset = UserData.objects.all()
    serializer_class = UserDataSerializer

class UserLogin(generics.CreateAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny] 

    def post(self, request, *args, **kwargs):
        data = request.data
        email = data.get("email")
        password = data.get("password")

      
        user = authenticate(email=email, password=password)

        if user is not None:
            refresh = RefreshToken.for_user(user)
            access_token = refresh.access_token

            return Response({
                "message": "Login Successful",
                "refresh": str(refresh),
                "access": str(access_token)
            }, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid Credentials"}, status=status.HTTP_400_BAD_REQUEST)

class EventListCreateAPI(generics.ListCreateAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventModelSerializer

class EventRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventModel.objects.all()
    serializer_class = EventModelSerializer
    
class EventRegAPI(generics.ListCreateAPIView):
    queryset = EventReg.objects.all()
    serializer_class = EventRegSerializer

class EventRegRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = EventReg.objects.all()
    serializer_class = EventRegSerializer
    
class ParticipantsAPI(generics.ListCreateAPIView):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer
    
 
class ParticipantsRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer  
      
class DigitalCertAPI(generics.ListCreateAPIView):
    queryset = DigitalCertificate.objects.all()
    serializer_class = DigitalCertificateSerializer
    
class ParticipantsRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Participants.objects.all()
    serializer_class = ParticipantsSerializer    
    
class DigitalCertRUDAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = DigitalCertificate.objects.all()
    serializer_class = DigitalCertificateSerializer