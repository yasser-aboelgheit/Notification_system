from rest_framework import serializers
from .models import Passenger
from django.contrib.auth.models import User

class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ['name',]
        model = Passenger


class PassengerRegisterSerializer(serializers.Serializer):
    username = serializers.EmailField(required=True)
    password = serializers.CharField(required=True)
    phone_number = serializers.CharField(required=True)
    name = serializers.CharField(required=True)
    home_address = serializers.CharField(required=True)
    work_address = serializers.CharField(required=True)
    notification_langauge = serializers.CharField(required=False)

    def validate_username(self, value):
        user = User.objects.filter(username=value)
        if user.count() != 0:
            raise serializers.ValidationError("this email is already registered", 409)
        return value