from rest_framework import serializers


class PromoCodeSerializer(serializers.Serializer):
    promo_code = serializers.CharField(required=True)
    expire_at = serializers.CharField(required=True)
