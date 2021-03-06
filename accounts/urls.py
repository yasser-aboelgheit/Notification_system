from django.urls import path
from .views import (PassengerAPIView, SelfRegisterViewSet)

urlpatterns = [
    path('passengers/', PassengerAPIView.as_view(), name='passengers'),
    path('passenger-register/', SelfRegisterViewSet.as_view(), name='passenger-register'),

]
