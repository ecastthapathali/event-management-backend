from rest_framework import serializers
from .models import UserData , EventModel , EventReg , Participants , DigitalCertificate

class UserDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["id", "name", "email", "phone_number", "password", "campus_name", "faculty"]

    def create(self, validated_data):
        user = UserData(
            email=validated_data['email'],
            name=validated_data['name'],
            phone_number=validated_data['phone_number'],
            campus_name=validated_data['campus_name'],
            faculty=validated_data['faculty'],
        )
        user.set_password(validated_data['password'])  
        user.save()
        return user

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.campus_name = validated_data.get('campus_name', instance.campus_name)
        instance.faculty = validated_data.get('faculty', instance.faculty)
        
        password = validated_data.get('password', None)
        if password:
            instance.set_password(password)
        
        instance.save()
        return instance
    
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserData
        fields = ["id","email","password"]

class EventModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventModel
        fields = "__all__"
        
class EventRegSerializer(serializers.ModelSerializer):
    class Meta:
        model = EventReg
        fields = "__all__"

class ParticipantsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participants
        fields = "__all__"
        
class DigitalCertificateSerializer(serializers.ModelSerializer):
    class Meta:
        model = DigitalCertificate
        fields = "__all__"
        