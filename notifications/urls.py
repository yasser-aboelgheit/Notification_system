
from django.urls import path
from .views import SendPromoAPIView

urlpatterns = [
    path('promo-codes/', SendPromoAPIView.as_view(), name='promo_codes'),
]
