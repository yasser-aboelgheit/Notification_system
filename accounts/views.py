from rest_framework import generics
from .models import Passenger
from .serializers import PassengerSerializer, PassengerRegisterSerializer
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from .celery_tasks import send_sms_on_register
import logging
logger = logging.getLogger('notify_logger')


class PassengerAPIView(generics.ListAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class SelfRegisterViewSet(generics.CreateAPIView):
    serializer_class = PassengerRegisterSerializer

    def create(self, *args, **kwargs):
        """
        creates new user and new passenger with active=True
        """
        request_body = self.request.data
        serializer = PassengerRegisterSerializer(data=request_body)
        if not serializer.is_valid():
            return Response(serializer.errors, 400)

        user = User.objects.create(
            username=serializer.validated_data["username"], email=serializer.validated_data["username"])
        user.set_password(request_body["password"])
        user.save()
        passengerProfile = Passenger.objects.create(user=user,
                                                    name=serializer.validated_data["name"],
                                                    username=serializer.validated_data["username"],
                                                    phone_number=serializer.validated_data["phone_number"],
                                                    home_address=serializer.validated_data["home_address"],
                                                    work_address=serializer.validated_data["work_address"],
                                                    notification_langauge=serializer.validated_data[
                                                        "notification_langauge"],
                                                    active=True,
                                                    )
        send_sms_on_register.s(
            passengerProfile.name, passengerProfile.phone_number).apply_async(queue="tasks")
        return Response({"message": "Account registration successful"}, status=201)
